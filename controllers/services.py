from typing import List, Optional

from controllers.schemas import ProductSchema


def filter_products(
    products: List[ProductSchema],
    best_seller: bool = False,
    rating_higher_than: Optional[str] = None,
    product_name: Optional[str] = None,
) -> List[ProductSchema]:
    """
    Filter products by the given parameters

    :param products: List of products
    :param best_seller: If True, returns only the best sellers
    :param rating_higher_than: If set, returns only the products with rating higher than the value
    :param product_name: If set, returns only the products with the name equal to the value
    :return: List of products
    """
    products_list_result: List[ProductSchema] = products
    for product in products_list_result[:]:
        should_to_remove = False
        if best_seller and not product.best_seller:
            should_to_remove = True
        if rating_higher_than and product.rating <= float(rating_higher_than):
            should_to_remove = True
        if product_name and product.name != product_name:
            should_to_remove = True
        if should_to_remove:
            products_list_result.remove(product)
    return products_list_result
