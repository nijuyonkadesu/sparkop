import json
from typing import List

import redis
from redis.commands.search import Search
from redis.commands.search.query import Query

from app.models.shoes import Product
from app.service.service_base import Service

class RedisService(Service):
    r: redis.Redis
    rs_shoes: Search 
    health = False

    def __init__(self):
        try: 
            self.r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
            self.rs_shoes = self.r.ft("idx:shoes")
            self.health = True
        except Exception as e: 
            print("unable to create redis client")
            self.health = False
            raise e

    def get_single_item(self, id: str) -> List[Product]:
        res: List[Product] = []
        color = "silver"
        products = self.rs_shoes.search(Query(f"@colors:{ {color} }").return_field("$"))

        for product in products.docs:
            shoe = product["json"]
            dict = json.loads(shoe)
            res.append(Product(**dict))

        return res


