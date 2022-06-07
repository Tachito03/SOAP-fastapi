from fastapi import FastAPI
from routes.api_soap import testSoap

app = FastAPI()

app.include_router(testSoap)

