from fastapi import FastAPI
from routes import test

app = FastAPI()
app.include_router(test.router)
