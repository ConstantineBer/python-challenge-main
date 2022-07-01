from typing import List

from bs4 import ResultSet
from pydantic import BaseModel

from controllers.base import BaseScrapper
from controllers.schemas import ProductSchema
from controllers.services import filter_products
from controllers.utils import get_text, perform_str_to_float, perform_rating_to_float


class ProductScrapper(BaseScrapper):
    def perform_data_to_model(
        self,
        products_list: ResultSet
    ) -> List[BaseModel]:
        """
        Performing the raw data to structured data.

        :param products_list: list of raw data with products
        :return: list of structured data with products
        """
        products: List[ProductSchema] = []
        for product in products_list:
            model_instance: ProductSchema = ProductSchema(
                name=get_text(
                    product.find(
                        "span", {"class": "a-size-base-plus a-color-base a-text-normal"}
                    )
                ),
                price=perform_str_to_float(
                    get_text(product.find("span", {"class": "a-price-whole"}))
                    + get_text(product.find("span", {"class": "a-price-fraction"}))
                ),
                rating=perform_rating_to_float(
                    get_text(product.find("span", {"class": "a-icon-alt"}))
                ),
                label=get_text(product.find("span", {"class": "a-badge-text"})),
            )
            products.append(model_instance)
        return products


def list_products(**kwargs) -> List[ProductSchema]:
    """
    Returns a list with all products in the page

    :param kwargs: best_seller: If True, returns only the best sellers
    :param kwargs: rating_higher_than: If set, returns only the products with rating higher than the value
    :param kwargs: product_name: If set, returns only the products with the name equal to the value
    :return: List of products
    """
    best_seller: bool = kwargs.get("best_seller", None)
    rating_higher_than: str = kwargs.get("rating_higher_than", None)
    product_name: str = kwargs.get("product_name", None)

    scrapper: ProductScrapper = ProductScrapper(
        "pages/content.html",
        "div",
        "sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20",
    )
    products_list_result: List[ProductSchema] = scrapper.products_list
    return filter_products(
        products_list_result,
        best_seller=best_seller,
        rating_higher_than=rating_higher_than,
        product_name=product_name,
    )


__all__: List[str] = [
    "list_products",
]
