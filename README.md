# great-usernames-api

The great usernames api is a api that provides usernames using a stripted down version of the <a href="https://github.com/akionsight/great-usernames">Great Usernames Engine</a>

This is a RESTful API to provide the features of the great usernames engine on the web, the <a href="https://github.com/akionsight/The-Great-Usernames-Website">Great Usernames website</a> is a good example of what can be done with this API

## Usage

The API is hosted on <a href="https://deta.sh">Deta</a> and is made with the **FastAPI framework**
Using the API is very simple. To get started you can 
- Follow the small guide below
- Check the Intercative docs with swagger ui @ https://n8w3zk.deta.dev/docs
- Check the interactive docs with redoc @ https://n8w3zk.deta.dev/redoc
 
### **THE BASE URL OF THE API IS https://n8w3zk.deta.dev**

#### Get a single username
To do this you can make a HTTP GET request on https://n8w3zk.deta.dev/get_one_username/ this endpoint. Here is some sample python code to get you started
```python

import requests

print(requests.get('https://n8w3zk.deta.dev/get_one_username/').json())

```

After executing, you may get a response like (the username generated each time will be new so dont worry if the usernames dont match because every username will be unique)

```json
{'username': 'confocal212'}
```

#### Get a number of usernames at the same time
This request can be made to do get multiple usernames at once. **WARNING: ONLY 20 USERNAMES WILL BE GENERATED AT ONCE, REQUSTING MORE THAN 20 WILL RAISE A HTTP 400 (BAD REQUEST) ERROR**

To do so you can make a HTTP GET request on the https://n8w3zk.deta.dev/get_a_number_of_usernames/ endpoint along with the number parameter

Some sample code to get you started 
```python
import requests

print(requests.get('https://n8w3zk.deta.dev/get_a_number_of_usernames/', {'number': 10}).json())
```

You can change the 'number' in the payload to anything between 1 and 20. After making the request, you may get a response like the following

```json
{'usernames': ['complacent876', 'stationarity935', 'infuse25', 'tutor659', 'Kendall743', 'dutiful596', 'Hinman206', 'Goa473', 'culinary168', 'biscuit662']}
``` 

This gives you a array of usernames. In this case we get 10 unique usernames because we requested two usernames

## For more info you can 

- Create a issue on this repo (I will be happy to answer your queries)
- go to the root url https://n8w3zk.deta.dev/ for some general info
- Go to the `/docs/` and `redoc/` urls listed above

## Self Hosting
for self hosting, refer <a href="https://github.com/akionsight/great-usernames-api/blob/main/SELF%20HOSTING.md">Self Hosting.md</a>

## Contributing
PR's are accepted, All PR's must be made on the dev branch. The source code for the API can be found in the <a href="https://github.com/akionsight/great-usernames-api/blob/main/great-usernames-api/main.py">The main.py inside the great usernames api folder</a>. To run the app on localhost, see <a href="/RUNNING ON LOCALHOST.md">Running on localhost</a>

