from abc import abstractmethod
from typing import List

from app.models.shoes import Product, RequestProduct


class Service():
    @abstractmethod
    def get_single_item(self, id: str) -> Product:
        pass

    @abstractmethod
    def get_latest_items(self, offset: int = 1, limit: int = 10) -> List[Product]:
        pass

    @abstractmethod
    def get_items(self, req: RequestProduct) -> List[Product]:
        pass
