# CybSafe Interview Exercise
by Eric Sales De Andrade (30 Nov 2021)

This is an exercise to build an API that can store Pokemon data 
from the Pokemon API - https://pokeapi.co/

## Architecture
The Repo contains
1. Script to scrape the Pokemon API
2. Script to create a Postgres Database, Table
3. Flask Application Wrapper around above 2 scripts
4. Docker Compose File to Host Web App and Database

## How To Run
### Step 1
In the Root Directory run
```
docker-compose up --build 
```
This will start the web service (by building and image off the 
Dockerfile) and the Postgres Database (by downloading the image
from the Dockerhub Repo)

### Step 2
Please check the Docker Logs for Unit Test. In a production 
setting with CI/CD we would stop the deployment if any Unit Test
Failed.

Once the docker compose successfully executes, paste the below 
URL in your browser or API Client to run the API. 

The API has 4 Endpoints
### 1. Test Endpoint
```
0.0.0.0:5000/
```
This is a test endpoint that returns a JSON message
```
{
    "Result": "Hello! Pokemon API is up and running"
}
```

### 2. Create Table Endpoint
```
0.0.0.0:5000/create_table
```
By making a GET request to this endpoint, we create a `pokemon` 
table with 4 columns - `pokemon_key` (uuid), `pokemon_id` 
(int, based off the id from the API URL), `pokemon_name` (str) 
and `pokemon_url` (str).

A successful API response is as below
```
{
    "Result": "Succeeded"
}
```

### 3. Store Pokemon Data
```
0.0.0.0:5000/store_pokemon?quantity=X
```
This endpoint gets `X` values as defined by the user 
(via a GET request parameter - `quantity`) and stores them
in the database.
A successful API response is as below
```
{
    "Result": "Succeeded"
}
```
### 4. Get Pokemon Data
```
0.0.0.0:5000/get_pokemon
```
This endpoint gets all values from the `pokemon` table. 
A successful API response is as below
```
{
    {
    "Result": "Succeeded",
    "records": [
        [
            "15a508a9-ef59-4857-b672-e9cb79ed5a6d",
            1,
            "bulbasaur",
            "https://pokeapi.co/api/v2/pokemon/1/"
        ],
        [
            "472cc9df-4a4f-4c61-90e3-f5e58ac25010",
            2,
            "ivysaur",
            "https://pokeapi.co/api/v2/pokemon/2/"
        ]...
]
}
```

## API Functionality Limitations
The following are limitations in the functionality of the API
1. The API doesn't support data UPDATES
2. The API only makes 1 call to the endpoint and can fetch 20
values in one execution.
3. The API retrieves all values from the database when
the `get_pokemon` endpoint is called.
4. The other Pokemon attributes and description is not stored 
and the setup uses just 1 Postgres table with 4 columns
5. The API doesn't have any security and Postgres has standard 
default username and password. 
   
## What I would implement for production
- Address the above limitations and extend API functionality.
- Fully comprehensive Unit and Integration tests to test
ALL API endpoints including connections to the Postgres DB.
- Package the script as a python module hosted in PackageCloud
or similar rather than just scripts. The CI/CD pipeline
would download this as a package and install
- Potentially rewrite the code to batch the SQL insert 
statements instead of writing each SQL statement individually
which makes the process inefficient.
- The detailed documentation and architecture diagrams.