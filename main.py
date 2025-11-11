from fastapi import FastAPI
import uvicorn

from client.app.run import start_app
from client.config.config import AppConfig, FastConfig
from api.users_router.router import user_router
from api.product_router.router import product_router
from api.caterory_router.router import category_router


app = FastAPI(title=FastConfig.title,
              description=FastConfig.description,
              version=FastConfig.version,
              lifespan=start_app
              )


app.include_router(user_router)
app.include_router(product_router)
app.include_router(category_router)


if __name__ == "__main__":
    uvicorn.run(
        app=AppConfig.app_name,
        host=AppConfig.host,
        port=AppConfig.port,
        reload=AppConfig.reload
        )
