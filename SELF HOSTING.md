# great-usernames-api

The great usernames api is a api that provides usernames using a stripted down version of the <a href="https://github.com/akionsight/great-usernames">Great Usernames Engine</a>

This is a RESTful API to provide the features of the great usernames engine on the web, the <a href="https://github.com/akionsight/The-Great-Usernames-Website">Great Usernames website</a>.


## Self-Hosting

I would recommend this if you want to host it for a larger project as I will not guarentee the uptime because I am on free hosting but it is very easy to deploy

The API is written on the **FastAPI framework** along with the **uvicorn ASGI framework** so there are plenty of hosting options out there so go out and choose your favoriate provider

To self host you need three files:
- main.py file (the actual source code)
- requirements.txt file (the requirements)
- names.txt (very important for the username generation)

These files can be found in the `great-usernames-api` directory. 

To host it on a VPS for example, you can install the requirements with the requirement.txt, place the main.py and names.txt in the same dir and start the server with the following commands

```
uvicorn main:app 
```
