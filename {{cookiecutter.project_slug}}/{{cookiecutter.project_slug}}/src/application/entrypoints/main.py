from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from application.adapters import orm
from application.adapters.database import create_engine_async_app
from application.entrypoints import users
from settings import config

app = FastAPI(title='Project Name')

orm.start_mappers()

(engine, sessionmaker) = create_engine_async_app(config.sqlalchemy_db)
app.state.engine = engine
app.state.sessionmaker = sessionmaker

app.add_middleware(SessionMiddleware, secret_key='!secret')

app.include_router(users.router)
