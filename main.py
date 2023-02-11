from fastapi import FastAPI
import sentry_sdk
import os

app = FastAPI()

if os.environ.get("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN"),
        traces_sample_rate=1.0,
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fail")
async def fail():
    raise RuntimeError("This is a failure")
