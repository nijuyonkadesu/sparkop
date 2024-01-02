from app.core.vars import app_health_status

def update_health(service_name: str):
    app_health_status[service_name] = True

