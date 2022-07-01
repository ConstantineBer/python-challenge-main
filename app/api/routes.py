from typing import List

from fastapi import APIRouter

from app.models.schemas.schemas import ProductResponseSchema
from controllers import main


router: APIRouter = APIRouter()


@router.get('/list_products', response_model=List[ProductResponseSchema], description='List products')
def list_products(best_seller=False, rating_higher_than=None, product_name=None) -> List[ProductResponseSchema]:
    """
    Returns a list with all products in the page

    :param best_seller: If True, returns only the best sellers
    :param rating_higher_than: If set, returns only the products with rating higher than the value
    :param product_name: If set, returns only the products with the name equal to the value
    :return: List of products
    """
    products = main.list_products(
        best_seller=best_seller,
        rating_higher_than=rating_higher_than,
        product_name=product_name
    )
    return [ProductResponseSchema(**product.dict()) for product in products]


_all__ = [
    'router',
]
