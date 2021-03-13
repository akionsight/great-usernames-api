from fastapi import FastAPI, status, Response
import constrains
import random


def generate_username():
    '''
    generates usernames 
    '''
    names = open(r'names.txt')
    names = names.read().replace('\n', ' ')
    names = names.split(' ')
    # finds a username from the list generated above
    username = random.choice(names) + str(random.randint(1, 999))
    return username


def get_all_usernames():
    names = open(r'names.txt')
    names = names.read().replace('\n', ' ')
    return names.split(' ')


app = FastAPI()


@app.get('/get_one_username/')
# @limiter.limit('5/minute')
async def return_a_single_username():
    """
    get a single username
    """
    name = generate_username()
    return {
        "username": name,
    }


@app.get('/starting_with/')
async def return_username_starting_with(letter: str, multiple: bool):
    names = get_all_usernames()
    usernames = []
    for i in names:
        if i.lower().startswith(letter.lower()):
            usernames.append(i)

    if multiple:
        return {
            'usernames': random.choices(usernames, weights=None, cum_weights=None, k=20)
        }
    else:
        return {
            'username': random.choice(usernames)
        }


@app.get('/ending_with/')
async def return_username_ending_with(letter: str, multiple: bool):
    names = get_all_usernames()
    usernames = []
    for i in names:
        if i.lower().endswith(letter.lower()):
            usernames.append(i)
    if multiple:
        return {
            'usernames': random.choices(usernames, weights=None, cum_weights=None, k=20)
        }
    else:
        return {
            'username': random.choice(usernames)
        }


@app.get('/get_a_number_of_usernames/')
async def return_a_specific_number_usernames(number: int, response: Response):
    """
    get a specific number of usernames
    """
    if number <= constrains.MAX_USERNAMES_PER_REQUEST and number > 0:
        usernames = []

        for _ in range(number):
            name = generate_username()
            usernames.append(name)

        return {
            'usernames': usernames
        }

    elif number <= 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "message": "0 usernames, literally"
        }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "message": f"too many usernames requested, a max of {constrains.MAX_USERNAMES_PER_REQUEST} can be requested at a single request"
        }


@app.get('/')
async def general_info():
    return {
        "message": "welcome to the great usernames api, all endpoints and docs urls are listed below",
        "intercative docs with swagger ui (credits to fastapi)": "/docs/",
        "interactive docs with redoc (credits to fastapi)": "/redoc/",
        "get one username": '/get_one_username/',
        f"get a number of usernames at once (maximum {constrains.MAX_USERNAMES_PER_REQUEST} can be obtained at once)": '/get_a_number_of_usernames/',
        "github repo": "https://github.com/akionsight/great-usernames-api"
    }
