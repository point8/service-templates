import random
from typing import Union

from fastapi_versioning import VersionedFastAPI, version

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
api = FastAPI()


@app.get("/")
def app_root():
    return {"Hello": "World"}


@api.get("/random")
@version(1)
def app_random():
    return [random.randrange(10) for i in range(10)]


@api.get("/items/{item_id}")
@version(1)
def app_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


api = VersionedFastAPI(api, version_format="{major}", prefix_format="/v{major}")

app.mount("/static", StaticFiles(directory="pdharcs/static"), name="static")
app.mount("/api", api)

ORIGINS = [
    "*",  # DO NOT USE IN PRODUCTION
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
)
