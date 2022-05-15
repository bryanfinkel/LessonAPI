# 5-14-22 Prior main file now called "main_v1.py" covers up to HW API 7
# prior to being split into multiple files:
# 1. main.py (new, simpler main file)
# 2. sub files that are called by main.py: greetings.py, sums.py, maths.py
# This is file greetings.py

from fastapi import APIRouter, FastAPI, status, HTTPException #APIRouter,
from pydantic import BaseModel

router = APIRouter()
app = FastAPI() # -- Q: Do we not need this line any more because we are using APIrouter now?

# GREETING APIs  -----------------------------------------------------------
# PATH = (none)
@app.get("/")
async def root():
    return {"message": "Running LessonAPI/main.py, just the slash"}

# API 1: GET /api/v1/ping -> return a pre-defined string
@app.get("/api/v1/ping")
async def ping():
    return {"message from ping": "pong"}

# API 2: GET /api/v1/greeting -> return a pre-defined key-value pair
@app.get("/api/v1/greeting")
async def greeting():
    return {"greeting": "Hello API 2"}

# API 3: GET /api/v1/greeting/pradeep -> input a path parameter and return a key-value pair using the parameter
@app.get("/api/v1/greeting/{pradeep}")        # remember the brackets for a parameter
async def Var_Name(pradeep):
    return {"greeting": "Hello API 3, this is "+pradeep}

#API 7: GET /api/v1/hello?name=pradeep -> use query params
# READ THE DOCS: https://fastapi.tiangolo.com/tutorial/query-params/
# use this URL to test: http://127.0.0.1:8000/api/v1/hello/?name=pradeep
@app.get("/api/v1/hello")
async def QueryPass(name: str = "World"): # World is the default if no query param is passed
    return{"greeting":"Hello "+name+"!"}



'''
--- START REFERENCE URLS  -------------------------
https://www.notion.so/Api-Exercise-8c8c0119b01642c1a8b35e9f5bfecf8c -> HW assignment
https://fastapi.tiangolo.com/tutorial/path-params/ -> FastAPI Path Parameters
--- END REFERENCE URLS  --------------------------- 
'''