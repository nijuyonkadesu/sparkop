from typing import List
from fastapi.routing import APIRouter
from app.core.utils import get_service

from app.models.shoes import Product, RequestProduct
from app.service.service_base import Service

router = APIRouter(prefix="/shoes", tags=["shoes"])
service: Service = get_service("redis") 

# TODO: use depends

@router.get("/{id}", response_model=Product)
def fetch_product(id: str):
    try:
        return service.get_single_item(id)
    except Exception as e:
        raise e

@router.post("/search", response_model=List[Product])
def fetch_products(req: RequestProduct):
    return service.get_items(req)

