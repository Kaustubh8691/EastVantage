from fastapi import FastAPI
from route.address import address
app = FastAPI()
app.include_router(address)