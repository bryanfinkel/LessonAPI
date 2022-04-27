from fastapi import FastAPI

app = FastAPI()

# START PRADEEP LESSON - SIMPLE APIs  -----------------------------------------------------------
@app.get("/")
async def root():
    return {"message": "Running LessonAPI/main.py, just the slash"}

# API 1: GET /api/v1/ping -> return a pre-defined string
@app.get("/api/v1/ping")
async def ping():
    return {"message from ping": "pong"}
# END PRADEEP LESSON - SIMPLE APIs  ------------------------------------------------------------


# START HOMEWORK -------------------------------------------------------------------------------

''' START REFERENCE URLS  -------------------------
https://www.notion.so/Api-Exercise-8c8c0119b01642c1a8b35e9f5bfecf8c -> HW assignment
https://fastapi.tiangolo.com/tutorial/path-params/ -> FastAPI Path Parameters
--- END REFERENCE URLS  --------------------------- 
'''

# API 2: GET /api/v1/greeting -> return a pre-defined key-value pair
@app.get("/api/v1/greeting")
async def greeting():
    return {"greeting": "Hello API 2"}

# API 3: GET /api/v1/greeting/pradeep -> input a path parameter and return a key-value pair using the parameter
@app.get("/api/v1/greeting/{pradeep}")        # remember the brackets for a parameter
async def Var_Name(pradeep):
    return {"greeting": "Hello API 3, this is "+pradeep}

# API 4: GET /api/v1/sum/1/1 --> input (2) path parameters, and them, and return the sum
'''first try -- did not work because V1,V2 are strings, so operator + executed a "concatenate"
@app.get("/api/v1/sum/{V1}/{V2}")
async def sum(V1,V2):
    BIF = V1 + V2
    VAR1 = V1
    VAR2 = V2
    VAR3= sum
    print (VAR3)
    return {"sum":VAR3}
'''
# second try -- Q: did I need to force the int on the parameters in the method, or just the formula?
@app.get("/api/v1/sum1/{V1}/{V2}")     # /sum1 forces parameters in 2 places - THIS WORKS
async def sum(V1: int,V2: int):
    VAR1=int(V1)
    VAR2=int(V2)
    # VAR3= sum --> remove this. sum is a method above, we can't refer to a method from inside the method
    # print (VAR3)
    BIF=VAR1+VAR2
    print(BIF)
    return {"Double forcing":BIF}

# second try continued -- several iterations to test ways to do the forcing
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

# END HOMEWORK ----------------------------------------------------------------------------------