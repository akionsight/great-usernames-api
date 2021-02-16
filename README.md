# great-usernames-api

The great usernames api is a api that provides usernames using a stripted down version of the <a href="https://github.com/akionsight/great-usernames">Great Usernames Engine</a>

This is a RESTful API to provide the features of the great usernames engine on the web, the <a href="https://github.com/akionsight/The-Great-Usernames-Website">Great Usernames website</a>.


## Self-Hosting

I would recommend this if you want to host it for a larger project as I will not guarentee the uptime because I am on free hosting but it is very easy to deploy

The API is written on the **FastAPI framework** so there are plenty of hosting options out there so go out and choose your favoriate

### Hosting on Deta

I would recommend <a href="https://deta.sh">Deta</a> as file structure required are already in there. to do so first <a href="https://www.deta.sh/">Create a Deta account</a> 

Then <a href="https://docs.deta.sh/docs/cli/install">Install the Deta Cli</a> and follow the instrctions to log in to the cli

Then Clone the repo with the following command 
```
git clone https://github.com/akionsight/great-usernames-api
```

Then cd into the `great-usernames-api` directory with the following command

```
cd great-usernames-api/great-usernames-api
```

Assuming you want everything in the default project, you can create a new Deta Micro with the following command

```
deta new --python great_usernames_api
```
The cli should respond with something like 
```
{
    "name": "great_usernames_api",
    "runtime": "python3.7",
    "endpoint": "https://<path>.deta.dev",
    "visor": "enabled",
    "http_auth": "enabled"
}
```
Save this, this is important

Its <strike>Showtime</strike> Deploy time. To deploy execute the deta deploy command

```
deta deploy
```

Now go to the endpoint you recieved while creating your micro and you should be good to go

## Hosting on other providers

to host on other providers, first clone the repo

```
git clone https://github.com/akionsight/great-usernames-api
```

now cd into the required directr
