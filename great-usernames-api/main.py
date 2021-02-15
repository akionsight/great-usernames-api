from fastapi import FastAPI, status, Response
import random



def generate_username():
    '''
    generates usernames 
    '''
    names = open(r'names.txt')
    names = names.read().replace('\n', ' ')
    names = names.split(' ')
    username = random.choice(names) + str(random.randint(1, 999)) ## finds a username from the list generated above
    return username

app = FastAPI()


@app.get('/get_one_username/')
# @limiter.limit('5/minute')
def return_a_single_username():
    """
    get a single username
    """
    name = generate_username()
    return {
        "username": name ,
        }

@app.get('/get_a_number_of_usernames/')
def return_a_specific_number_usernames(number: int, response: Response):
    """
    get a specific number of usernames
    """
    if number <= 20 and number > 0:
        usernames = []

        for _ in range(number):
            name = generate_username()
            usernames.append(name)

        return {
            'usernames': usernames
        }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "message": "too many usernames requested, a max of 20 can be requested at a single request"
        }
@app.get('/')
async def general_info():
    return {
        "message": "welcome to the great usernames api, all endpoints and docs urls are listed below",
        "intercative docs with swagger ui (credits to fastapi)": "/docs/",
        "interactive docs with redoc (credits to fastapi)" : "/redoc/",
        "get one username": '/get_one_username/',
        "get a number of usernames at once (maximum 20 can be obtained at once)": '/get_a_number_of_usernames/',
        "github repo": "https://github.com/akionsight/great-usernames-api"
    }