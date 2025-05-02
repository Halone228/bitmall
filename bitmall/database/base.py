from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from os import environ
from sqlalchemy.engine.url import URL

assert environ.get("DB_HOST"), "No DB_HOST"
assert environ.get("DB_PORT"), "No DB_PORT"
assert environ.get("DB_USERNAME"), "No DB_USERNAME"
assert environ.get("DB_PASSWORD"), "No DB_PASSWORD"
assert environ.get("DB_NAME"), "No DB_NAME"


url = URL.create(
    drivername='psycopg_async',
    host=environ.get("DB_HOST"),
    port=int(environ.get("DB_PORT") or 0),
    username=environ.get("DB_USERNAME"),
    password=environ.get("DB_PASSWORD"),
    database=environ.get("DB_NAME")
)

engine = create_async_engine(
    url
)
sessionmaker = async_sessionmaker(engine)
