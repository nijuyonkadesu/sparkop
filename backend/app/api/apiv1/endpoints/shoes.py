

from typing import List
from fastapi.routing import APIRouter

from app.models.shoes import Product, ProductInfo, Prices
from app.service.redis_service import RedisService


router = APIRouter(prefix="/shoes", tags=["shoes"])
service = RedisService()

# TODO: use depends

@router.get("/{id}", response_model=List[Product])
def fetch_product(id: str) -> List[Product]:

    return service.get_single_item(id)
    # TODO: return http errors in failure cases


