from fastapi import APIRouter

from config.constants import TAG_COMMON

router = APIRouter(tags=[TAG_COMMON])
