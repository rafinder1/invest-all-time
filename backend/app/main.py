from fastapi import FastAPI
from api.endpoints import prices

app = FastAPI()

app.include_router(prices.router, prefix="/api/v1/prices", tags=["prices"])
