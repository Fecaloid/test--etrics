from fastapi import APIRouter

from config.constants import TAG_METRIC

router = APIRouter(tags=[TAG_METRIC])
