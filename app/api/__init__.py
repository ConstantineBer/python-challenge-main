from fastapi import APIRouter

from app.api.routes import router as product_router


router: APIRouter = APIRouter()

router.include_router(product_router, tags=["products"])


__all__ = [
    "router",
]
