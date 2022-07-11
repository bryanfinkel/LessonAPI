# 7-10-22 Lesson on Authentication
# This is file auth.py

from fastapi import APIRouter


router = APIRouter()
# WE HAVE LINE ABOVE --> router = APIRouter(), SO --> REPLACE APP.GET WITH ROUTER.GET BELOW...

# AUTH APIs  -----------------------------------------------------------

import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# replace THIS: app = FastAPI() with THAT: router = APIRouter() ie, see above, line 7

security = HTTPBasic()

# ------------------------------------------------------------------------------------------------------------
# First simple example - this works: http://127.0.0.1:8000/users/me returns to brower the name and password
# @app.get("/users/me") -- replacing app with router
@router.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Second example, check the username and password against stored credentials
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "bryan")
    correct_password = secrets.compare_digest(credentials.password, "apilesson")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        #return {"explanation":"incorrect username or password"}
        #return detail
        # Pradeep: how can I return an error explanation to the browser window?
        )
    return credentials.username


# change app to router: @app.get("/users/me")
@router.get("/users/me2")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}

# ------------------------------------------------------------------------------------------------------------