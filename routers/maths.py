# 5-14-22 Prior main file now called "main_v1.py" covers up to HW API 7
# prior to being split into multiple files:
# 1. main.py (new, simpler main file)
# 2. sub files that are called by main.py: greetings.py, sums.py, maths.py
# This is file maths.py

from fastapi import APIRouter, FastAPI, status, HTTPException
from pydantic import BaseModel

router = APIRouter()
app = FastAPI() # -- Q: Do we not need this line any more because we are using APIrouter now?

# START HOMEWORK APIs 5 6 7 ---------------------------------------------------------------------

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
        raise HTTPException(status_code=404, detail="Item not found in this program")

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

# API 6: POST /api/v1/math/{operation} -> execute +,-,*,/ or return 404 if operation invalid
# First POST, not a GET
# /api/v1/math/add/1/2

# following class taken from pydantic
class Item(BaseModel):
    variable1: int
    variable2: int

# First POST, not a GET
@app.post("/api/v1/math/{operation}")
async def PerformOperation6(operation: str, item: Item):
    variable1: int = item.variable1
    variable2: int = item.variable2
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
--- START REFERENCE URLS  -------------------------
https://www.notion.so/Api-Exercise-8c8c0119b01642c1a8b35e9f5bfecf8c -> HW assignment
https://fastapi.tiangolo.com/tutorial/path-params/ -> FastAPI Path Parameters
--- END REFERENCE URLS  --------------------------- 
'''

'''
@app.post("/trees/")
async def create_trees(item: Item):
    return item
@app.post("/api/v1/math/{operation}/items/")
async def PerformOperation6(operation: str, item: Item):
async def PerformOperation6(item: Item):
'''