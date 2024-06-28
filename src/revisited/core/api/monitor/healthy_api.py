import logging

from fastapi import APIRouter

from .models import HealthyStatusModel

healthy_router = APIRouter()

logger = logging.getLogger(__name__)


@healthy_router.post("/healthy", status_code=200, response_model=HealthyStatusModel,tags=['monitor'])
async def healthy() -> HealthyStatusModel:
    logger.info(f"Incoming Request: Healthy ")
    return HealthyStatusModel()
