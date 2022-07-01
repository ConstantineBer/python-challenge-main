import http
from typing import List, Dict, Union

from fastapi.testclient import TestClient
from requests import Response

from tests.app.api.mocks import (
    products_result,
    products_result_best_seller,
    products_result_rating_higher_than,
    products_result_product_name,
    products_result_rating_higher_than_and_best_seller,
)
from app.main import app


client: TestClient = TestClient(app)


def test_list_products_success() -> None:
    # Arrange
    url: str = '/list_products'

    # Act
    response: Response = client.get(url)
    as_is: List[Dict[str, Union[bool, float, str]]] = response.json()
    desired_result: List[Dict[str, Union[bool, float, str]]] = products_result

    # Assert
    assert response.status_code == http.HTTPStatus.OK
    assert as_is == desired_result


def test_list_products_success_best_seller() -> None:
    # Arrange
    url: str = '/list_products?best_seller=true'

    # Act
    response: Response = client.get(url)
    as_is: List[Dict[str, Union[bool, float, str]]] = response.json()
    desired_result: List[Dict[str, Union[bool, float, str]]] = products_result_best_seller

    # Assert
    assert response.status_code == http.HTTPStatus.OK
    assert as_is == desired_result


def test_list_products_success_rating_higher_than() -> None:
    # Arrange
    url: str = '/list_products?rating_higher_than=4.8'

    # Act
    response: Response = client.get(url)
    as_is: List[Dict[str, Union[bool, float, str]]] = response.json()
    desired_result: List[Dict[str, Union[bool, float, str]]] = products_result_rating_higher_than

    # Assert
    assert response.status_code == http.HTTPStatus.OK
    assert as_is == desired_result


def test_list_products_success_product_name() -> None:
    # Arrange
    url: str = '/list_products?product_name=Smartphone+Poco+X3+PRO+128gb+6gb+RAM+–+Phantom+Black+-+Preto'

    # Act
    response: Response = client.get(url)
    as_is: List[Dict[str, Union[bool, float, str]]] = response.json()
    desired_result: List[Dict[str, Union[bool, float, str]]] = products_result_product_name

    # Assert
    assert response.status_code == http.HTTPStatus.OK
    assert as_is == desired_result


def test_list_products_success_rating_higher_than_and_best_seller() -> None:
    # Arrange
    url: str = '/list_products?rating_higher_than=4.7&best_seller=true'

    # Act
    response: Response = client.get(url)
    as_is: List[Dict[str, Union[bool, float, str]]] = response.json()
    desired_result: List[Dict[str, Union[bool, float, str]]] = (
        products_result_rating_higher_than_and_best_seller
    )

    # Assert
    assert response.status_code == http.HTTPStatus.OK
    assert as_is == desired_result
