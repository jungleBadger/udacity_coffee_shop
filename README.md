# Coffee Shop Full Stack

## Full Stack Nanodegree


### Auth0 account
```
AUTH0_DOMAIN = 'junglebadger.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'https://junglebadger.github.io'
```

> :warning: I DID updated the POSTman collection with both `barista` and `manager` accounts, the thing is that the token does expire, so I've created two dummy accounts on my Auth0 profile, both of them are verified and functional.

#### Manager account
```
User: coffee_manager@udacity.com
password: udacity123*
submitted token (which can be expired at the time of review - "2019-07-09T14:49:45.778Z"): 
```
`eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlJEYzJSa05HUmtSRk1rVkJOMEl4TkVFeE1rUkRRemswTTBRMU4wTTRSRVZFT0VSRk1qWkJSUSJ9.eyJpc3MiOiJodHRwczovL2p1bmdsZWJhZGdlci5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWQyNGEzZTA2YzM3MDMwZDc0ZDA4NjJkIiwiYXVkIjoiaHR0cHM6Ly9qdW5nbGViYWRnZXIuZ2l0aHViLmlvIiwiaWF0IjoxNTYyNjgzNzA5LCJleHAiOjE1NjI2OTA5MDksImF6cCI6Ik9hcXNrSWRpVXQwN25Eem45SGpuVEdPU3ExSUI1OUtEIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.OqhFINSM0FogbYCq3e8LYa-hcHFFEmUNLDPuSeLpzYWgoOCiPzv_OpIYAa2s0TU3el2r8FJxNWT3Pk0st_sPvNOaPXga9jPSJiLfp3DdT60dy8MrI3bn1VW_7UpnUjimIxzedf79MRHXbw3lviBcpvxsTmVp_WYAG1nTMbN9ShcOLGBdw-2N_71lB_2_rRqiE6nwDvh52g4LZPSdIUQCJLdGjSAWrrcaYLU4mA8SpNf_IkC-wmKHSx_nceCFyWU5tNsXy_lARVXEfjS_zSTDlF_N8mLeufL05yCrQR8QTo_BGbf7zXzIZwmyuTe1YCBnI5PrrCZufsINH24BHAdfZw`


#### Barista account
```
User: barista@udacity.com
password: udacity123*
submitted token (which can be expired at the time of review - "2019-07-09T14:52:13.496Z"):
```
`eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlJEYzJSa05HUmtSRk1rVkJOMEl4TkVFeE1rUkRRemswTTBRMU4wTTRSRVZFT0VSRk1qWkJSUSJ9.eyJpc3MiOiJodHRwczovL2p1bmdsZWJhZGdlci5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWQyNGEzYmMxOWZlOTQwYzhiNzY4NjY2IiwiYXVkIjoiaHR0cHM6Ly9qdW5nbGViYWRnZXIuZ2l0aHViLmlvIiwiaWF0IjoxNTYyNjgzODE4LCJleHAiOjE1NjI2OTEwMTgsImF6cCI6Ik9hcXNrSWRpVXQwN25Eem45SGpuVEdPU3ExSUI1OUtEIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.0M4z2WqcSekcZDUczXMxRg-HS9_a2jsornHd1B7ew-6tl99JVRtgXDA_-pKpd0fs1F2yvoAaUjqBgY_iayAAxlHqef1RlskBzB-LpgMc3Af26p7XIZ5kBNXOrIzyBYyctzWdZ7niVUdAzTuZwCotGMeof-hh5kRZlMf9JXtvco7Cqd3g_LrXpGb41pP3nxm-Mpiy2KW0KcHjD1KZ_1lFkQcbPHz1W7m3E4cEINYFjFWgxumJhLsmZh1_9hMiRz8gd0FL349uCp9ccHFz01U_KYS0ZbGc2i2J0jSrhaNumRyduxpTSl4r963Uf40L0jNoX-bEFBhL4JyovizBgIjJiw`


### POSTman

* Exported collection with configured tokens can be found at: `/backend/udacity-fsnd-udaspicelatte.postman_collection_STUDENT_TOKEN.json`
* Test results containing 20 successful cases: `/backend/udacity-fsnd-udaspicelatte.postman_collection_test_run.json`
* Seed collection remains untouched 


### Backend

* Added Auth0 functionalities
* Implemented RESTful endpoints
* Implemented error handlers
* I've used [YAPF](https://github.com/google/yapf) to enforce python code style

#### Running the app

1. Install dependencies with `pip install -r backend/requirements.txt`
2. Set the `FLASK_APP` variable running `export FLASK_APP=api.py` 
3. Run the app with `flask run --reload`

### Frontend 

* Added the Auth0 variables on `environment.ts` file
* Guarantee that the frontend can be launched upon an `ionic serve` command and the login/token retrieval are functional



### .gitignore

* Added jetbrains folder

### Resources
* https://github.com/udacity/FSND/tree/master/BasicFlaskAuth
* https://github.com/auth0-samples/auth0-python-api-samples/tree/master/00-Starter-Seed