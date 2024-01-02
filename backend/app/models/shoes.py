from dataclasses import dataclass


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
 


