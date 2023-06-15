from fastapi import APIRouter

from config.constants import TAG_PROBES

router = APIRouter(tags=[TAG_PROBES])
