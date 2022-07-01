from typing import List

from bs4 import BeautifulSoup, ResultSet
from pydantic import BaseModel


class BaseScrapper:
    def __init__(
        self,
        url: str,
        html_tag: str,
        classes_to_search: str,
        model: BaseModel,
    ) -> None:
        """
        :param url: url of the html page
        :param html_tag: html tag to search products of e-commerce site
        :param classes_to_search: classes to search products of e-commerce site
        :param model: pydantic model to struct the products
        """
        self.html_page_url = url
        self.html_tag = html_tag
        self.classes_to_search = classes_to_search
        self.model = model
        self.products_list = self.__perform()

    def __perform(self) -> List[BaseModel]:
        """
        Life cycle method to perform data to models.

        :return: list of products
        """
        with open(self.html_page_url, 'r') as f:
            soup: BeautifulSoup = BeautifulSoup(f.read(), 'html.parser')
            products_list: ResultSet = self.__get_product_entities_by_class(
                soup,
                self.html_tag,
                self.classes_to_search
            )
            return self.perform_data_to_model(products_list, self.model)

    def perform_data_to_model(
        self,
        products_list: ResultSet,
        model: BaseModel,
    ) -> List[BaseModel]:
        """
        Performing the raw data to structured data.

        :param products_list: list of raw data with products
        :param model: pydantic model to struct the products
        :return: list of structured data with products
        """
        raise NotImplementedError

    @staticmethod
    def __get_product_entities_by_class(soup: BeautifulSoup, html_tag: str, classes_to_search: str) -> ResultSet:
        """
        Get the product entities by class.

        :param soup: BeautifulSoup object with the html page
        :param html_tag: html tag to search products of e-commerce site
        :param classes_to_search: classes to search products of e-commerce site
        :return: list of raw products
        """
        products_list: ResultSet = soup.find_all(html_tag, {'class': classes_to_search})
        return products_list


__all__: List[str] = [
    'BaseScrapper',
]
