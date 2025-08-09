
from fastapi import FastAPI
from core.db import init_db

from routes import user


app = FastAPI()

@app.on_event('startup')
async def start_db():
    await init_db()


from core import handlers, middlewares


app.include_router(user.router)

@app.get('/')
async def hello_world():
    return {
        "message": "hello world from FastAPI!"
    }

