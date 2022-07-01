from typing import Optional, List

from bs4 import BeautifulSoup


def perform_str_to_float(value: str) -> float:
    try:
        val: float = float(value.replace(".", "").replace(",", "."))
    except ValueError as e:
        raise e
    return val


def perform_rating_to_float(value: str) -> float:
    try:
        val: float = float(value.split(" ")[0].replace(",", "."))
    except ValueError as e:
        raise e
    return val


def get_text(element: BeautifulSoup) -> Optional[str]:
    if element is not None:
        return " ".join(element.text.split())
    return None


__all__: List[str] = [
    "perform_str_to_float",
    "perform_rating_to_float",
    "get_text",
]
