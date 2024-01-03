import time
from functools import wraps
from app.service.redis_service import RedisService

from app.service.service_base import Service

def retry_on_exception(retries = 15, delay=0.3):
   def decorator(func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           for _ in range(retries):
               try:
                  return func(*args, **kwargs)
               except Exception as e:
                   print(e, "trying again to get service instance...")
                   time.sleep(delay)
       return wrapper
   return decorator

def get_service(name: str) -> Service:
    if name == "redis":
        return RedisService()
    else:
        raise Exception("Invalid service name")
