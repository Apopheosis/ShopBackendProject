from os import environ
from starlette.config import Config

import databases

config = Config(".env")

DB_USER = config('DB_USER', cast=str)
DB_PASSWORD = config('DB_PASSWORD', cast=str)
DB_HOST = config('DB_HOST', cast=str)
DB_PORT = config('DB_PORT', cast=str)
DB_NAME = config('DB_NAME', cast=str)

TESTING = environ.get("TESTING")

if TESTING:
    DB_NAME = 'async-cart-temp-for-test'
    TEST_SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    )
    database = databases.Database(TEST_SQLALCHEMY_DATABASE_URL)
else:
    DB_NAME = "shop_database"
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    database = databases.Database(SQLALCHEMY_DATABASE_URL)