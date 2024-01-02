from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class Prices:
    amountMax: float
    amountMin: float
    dateAdded: int


@dataclass
class ProductInfo:
    brand: str
    colors: str
    categories: str
    name: str
    prices: Prices
 
# ----------------- PUBLIC CLASS ----------------- #

@dataclass
class Product:
    id: str
    dateAdded: int
    dateUpdated: int
    productInfo: ProductInfo
 

# the requests made into the api should be a pydantic class
class RequestProduct(BaseModel):
    color: str
    brand: str
    categories: str
    offset: int = 0
    limit: int = 10

