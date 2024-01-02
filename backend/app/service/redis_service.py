import json
from typing import List

import redis
from redis.commands.search import Search
from redis.commands.search.query import Query
from app.api.deps import update_health

from app.models.shoes import Product, RequestProduct
from app.service.service_base import Service

class RedisService(Service):
    r: redis.Redis
    rs_shoes: Search 

    def __init__(self):
        try: 
            self.r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
            self.rs_shoes = self.r.ft("idx:shoes")
            update_health("redis")
        except Exception as e: 
            print("unable to create redis client")
            self.health = False
            raise e

    def get_single_item(self, id: str) -> Product:
        product = self.r.json().get("product:" + id)
        return Product(**product) 

    def get_items(self, req: RequestProduct) -> List[Product]:
        res: List[Product] = []
        products = self.rs_shoes \
                .search(Query(f"@colors:{ {req.color} } @brand:{ {req.brand} } {req.categories} ") \
                .paging(req.offset, req.limit) \
                .return_field("$"))

        for product in products.docs:
            shoe = product["json"]
            dict = json.loads(shoe)
            res.append(Product(**dict))

        return res

# TODO: server crashes if brand string is "*"
# TODO: make some search options optional
