from typing import Optional

from pydantic import BaseModel


class ProductResponseSchema(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    rating: Optional[float] = None
    best_seller: Optional[bool] = None


__all__ = [
    "ProductResponseSchema",
]
