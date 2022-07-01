import uvicorn
from fastapi import FastAPI

from app.settings import settings
from app.api import router


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.PROJECT_VERSION
    )
    application.include_router(router)
    return application


app: FastAPI = get_application()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
