from typing import List

from app.models.shoes import Product


class Service():
    def get_single_item(self, id: str) -> List[Product]:
        pass

    def get_latest_items(self, offset: int = 1, limit: int = 10) -> List[Product]:
        pass
