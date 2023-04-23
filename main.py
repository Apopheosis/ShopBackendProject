from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from models.database import database
from routers import items_router, users_router, orders_router

app = FastAPI(debug=True)

app.include_router(items_router.router)
app.include_router(users_router.router)
app.include_router(orders_router.router)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi_schema = custom_openapi()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()




