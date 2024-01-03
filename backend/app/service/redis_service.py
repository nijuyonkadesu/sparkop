import json
from typing import List
from fastapi import HTTPException

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
            self.r.ping()
            self.rs_shoes = self.r.ft("idx:shoes")
            update_health("redis")
        except Exception as e: 
            print("faulty redis client connection, check host / port etc", e)
            self.health = False
            # raise e

    def get_single_item(self, id: str) -> Product:
        product = self.r.json().get("product:" + id)
        if product is None:
            raise HTTPException(status_code=404, detail="Item not found") 
        else: 
            return Product(**product) 

    def get_items(self, req: RequestProduct) -> List[Product]:
        def preprocess_spl_chars(s: str):
            # return "".join(["\\" + c if not c.isalnum() else c for c in s])
            return s

        res: List[Product] = []
        params = ""
        if len(req.brand) > 0:
            params += f"@brand:{ {preprocess_spl_chars(req.brand)} } "
        if req.color.isalnum():
            params += f"@colors:{ {req.color} } "
        params += f"{preprocess_spl_chars(req.categories)} "
        print(f"params: >{params}<", f"req: >{req}<")

        products = self.rs_shoes \
                .search(Query(params) \
                .paging(req.offset, req.limit) \
                .return_field("$"))

        for product in products.docs:
            shoe = product["json"]
            dict = json.loads(shoe)
            res.append(Product(**dict))

        return res

# WARNING: redis search with special characters is a bad idea. It's a endless conflit with raw and formatted string. I couldn't find a fix
