from pydantic import BaseModel

from apps.healthcheck.enums import StatusEnum


class HealthcheckServiceResult(BaseModel):
    status: StatusEnum
    service: str
    message: str = ''


class HealthcheckResult(BaseModel):
    status: StatusEnum
    details: list[HealthcheckServiceResult]
