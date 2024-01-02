

from typing import List
from fastapi.routing import APIRouter

from app.models.shoes import Product, ProductInfo, Prices, RequestProduct
from app.service.redis_service import RedisService
from app.service.service_base import Service

router = APIRouter(prefix="/shoes", tags=["shoes"])
service: Service = RedisService()

# TODO: use depends

@router.get("/{id}", response_model=Product)
def fetch_product(id: str) -> Product:
    return service.get_single_item(id)

@router.post("/search", response_model=List[Product])
def fetch_products(req: RequestProduct) -> List[Product]:
    return service.get_items(req)


# TODO: return http errors in failure cases
