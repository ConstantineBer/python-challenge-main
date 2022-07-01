from typing import List, Dict, Union, Optional

from pydantic import BaseModel, validator

BEST_SELLER_STR: str = 'Mais vendido'


class ProductSchema(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    rating: Optional[float] = None
    label: Optional[str] = None
    best_seller: Optional[bool] = None

    @validator('best_seller', always=True)
    def set_best_seller(cls, value: str, values: Dict[str, Union[str, float, bool]]) -> bool:
        """
        Returns True if label is equal to Mais vendido.
        """
        return True if values['label'] == BEST_SELLER_STR else False


__all__: List[str] = [
    'ProductSchema',
]
