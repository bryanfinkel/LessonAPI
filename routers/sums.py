# 5-14-22 Prior main file now called "main_v1.py" covers up to HW API 7
# prior to being split into multiple files:
# 1. main.py (new, simpler main file)
# 2. sub files that are called by main.py: greetings.py, sums.py, maths.py
# This is file sums.py

from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

router = APIRouter()
app = FastAPI() # -- Q: Do we not need this line any more because we are using APIrouter now?

# SUM APIs  -----------------------------------------------------------
# API 4: GET /api/v1/sum/1/1 --> input (2) path parameters, and them, and return the sum

# sum1 - (my second try)  -- Q: did I need to force the int on the parameters in the method, or just the formula?
@app.get("/api/v1/sum1/{V1}/{V2}")     # /sum1 forces parameters in 2 places - THIS WORKS
async def sum(V1: int,V2: int):
    VAR1=int(V1)
    VAR2=int(V2)
    # VAR3= sum --> remove this. sum is a method above, we can't refer to a method from inside the method
    # print (VAR3)
    BIF=VAR1+VAR2
    print(BIF)
    return {"Double forcing":BIF}

@app.get("/api/v1/sum2/{V1}/{V2}")     # /sum2 no forcing is used - DOES NOT WORK, it concatenates V1 and V2
async def sum(V1,V2):
    VAR1=V1
    VAR2=V2
    BIF=VAR1+VAR2
    print(BIF)
    return {"NO forcing":BIF}

@app.get("/api/v1/sum3/{V1}/{V2}")     # /sum3 forces parameters in the method definition only - THIS WORKS
async def sum(V1: int,V2: int):
    VAR1=V1
    VAR2=V2
    BIF=VAR1+VAR2
    print(BIF)
    return {"Forcing in the method":BIF}

@app.get("/api/v1/sum4/{V1}/{V2}")     # /sum4 forces parameters in the VAR definitions only - THIS WORKS
async def sum(V1,V2):
    VAR1=int(V1)
    VAR2=int(V2)
    BIF=VAR1+VAR2
    print(BIF)
    return {"forcing at the variables":BIF}

@app.get("/api/v1/sum5/{V1}/{V2}")     # /sum5 eliminates unnecessary variables, forces parameters in the formula - THIS WORKS
async def sum(V1,V2):
    BIF = int(V1) + int(V2)
    print(BIF)
    return {"forcing in the forumula":BIF}


'''
--- START REFERENCE URLS  -------------------------
https://www.notion.so/Api-Exercise-8c8c0119b01642c1a8b35e9f5bfecf8c -> HW assignment
https://fastapi.tiangolo.com/tutorial/path-params/ -> FastAPI Path Parameters
--- END REFERENCE URLS  --------------------------- 
'''
'''
first try -- did not work because V1,V2 are strings, so operator + executed a "concatenate"
@app.get("/api/v1/sum/{V1}/{V2}")
async def sum(V1,V2):
    BIF = V1 + V2
    VAR1 = V1
    VAR2 = V2
    VAR3= sum
    print (VAR3)
    return {"sum":VAR3}
'''