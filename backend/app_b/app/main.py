from fastapi import FastAPI
from routes import test, kafka

app = FastAPI()
app.include_router(test.router)
app.include_router(kafka.router)
