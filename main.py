# 5-14-22 Prior main file now called "main_v1.py" covers up to HW API 7
# prior to being split into multiple files:
# 1. main.py (new, simpler main file)
# 2. sub files that are called by main.py: greetings.py, sums.py, maths.py

from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

# from app.respond_io.api.routes import router as respond_io_routes -- each segment is a folder down to routs.
# from app.intelepeer.api.routes import router as intelepeer_routes -- another example
# examples from Pradeep main.py

from routers.greetings import router as HW_greetings
from routers.sums import router as HW_sums
from routers.maths import router as HW_maths

app = FastAPI()
app.include_router(HW_greetings)
app.include_router(HW_sums)
app.include_router(HW_maths)

@app.get("/status")
async def status():
    return {"status": "up"}

