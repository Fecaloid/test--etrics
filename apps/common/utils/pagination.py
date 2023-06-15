from fastapi import Query
from fastapi_pagination import Params

from config.constants import PAGE_SIZE


class ModifiedParams(Params):
    size: int = Query(PAGE_SIZE, ge=1, le=100, description='Page size')
