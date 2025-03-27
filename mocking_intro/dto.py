from enum import StrEnum

import pydantic


class HealthState(StrEnum):
    OK = "OK"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class Healthcheck(pydantic.BaseModel):
    database: HealthState
    cache: HealthState
    queue: HealthState
    overall: HealthState
