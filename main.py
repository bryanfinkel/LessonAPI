from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# HTTPException from fastapi import HTTPException.
# added the import of HTTPException from this article https://fastapi.tiangolo.com/tutorial/handling-errors/

app = FastAPI()

# START HOMEWORK APIs 5 6 7 ---------------------------------------------------------------------
''' START REFERENCE URLS  -------------------------
NOTION https://www.notion.so/Api-Exercise-8c8c0119b01642c1a8b35e9f5bfecf8c
https://fastapi.tiangolo.com/tutorial/body/
--- END REFERENCE URLS  --------------------------- 
'''
# API 5: GET /api/v1/math/{operation}/{variable1}/(variable2} -> execute +,-,*,/ or return 404 if operation invalid
# /api/v1/math/add/1/2
@app.get("/api/v1/math/{operation}/{variable1}/{variable2}")
async def PerformOperation5(operation: str,variable1: int,variable2: int):
    if operation == "add":
        ops=variable1+variable2
        return {"ops": ops}
    elif operation == "sub":
        ops = variable1 - variable2
        return {"ops": ops}
    elif operation == "mult":
        ops = variable1 * variable2
        return {"ops": ops}
    elif operation == "div":
        ops = variable1 / variable2
        return {"ops": ops}
    else:
        print("else branch")
        raise HTTPException(status_code=404, detail="Item not found")

'''
To do later - create this endpoint with a dictionary -> 
def add (X,Y):
       return X+Y
   def sub (X,Y):
       return X-Y
   def mult (X,Y):
       return X*Y
   def div (X,Y):
       return X/Y

# I think I should use a dictionary here, but I need to relearn that - so using elif
   def OperationSelector(Ops, X, Y):
       if ops == "add":
           return add(X, Y)
       if ops == "sub":
           return sub(X, Y)
       if ops == "mult":
           return mult(X, Y)
       if ops == "div":
           return div(X, Y)
       else:
           return "unknown operator - 404 error"
   OperationSelector(operation,variable1,variable2)
'''
#return {test:"testing api 5"}


#API 6: POST /api/v1/math/{operation} -> execute +,-,*,/ or return 404 if operation invalid
# First POST, not a GET
# API 5: GET /api/v1/math/{operation}/{variable1}/(variable2} -> execute +,-,*,/ or return 404 if operation invalid
# /api/v1/math/add/1/2
@app.post("/api/v1/math/{operation}")
async def PerformOperation6(operation: str,variable1: int,variable2: int):
    if operation == "add":
        ops=variable1+variable2
        return {"ops": ops}
    elif operation == "sub":
        ops = variable1 - variable2
        return {"ops": ops}
    elif operation == "mult":
        ops = variable1 * variable2
        return {"ops": ops}
    elif operation == "div":
        ops = variable1 / variable2
        return {"ops": ops}
    else:
        print("else branch")
        raise HTTPException(status_code=404, detail="Item not found")



# END HOMEWORK APIs 5 6 7 -----------------------------------------------------------------------
#
#
#

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