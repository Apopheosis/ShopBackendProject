import os
from os import environ
from starlette.config import Config
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

import databases

config = Config(".env")

DB_USER = config('DB_USER', cast=str)
DB_PASSWORD = config('DB_PASSWORD', cast=str)
DB_HOST = config('DB_HOST', cast=str)
DB_PORT = config('DB_PORT', cast=str)

DB_NAME = "shop_database"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
if not database_exists(SQLALCHEMY_DATABASE_URL):
    create_database(SQLALCHEMY_DATABASE_URL)
database = databases.Database(SQLALCHEMY_DATABASE_URL)