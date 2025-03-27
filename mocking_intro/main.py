from fastapi import FastAPI

from mocking_intro.dto import Healthcheck, HealthState

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return {"Hello": "World"}


@app.get("/healthcheck")
async def healthcheck() -> Healthcheck:
    return Healthcheck(
        database=HealthState.OK,
        cache=HealthState.OK,
        queue=HealthState.OK,
        overall=HealthState.OK,
    )
