from fastapi import status
from fastapi.responses import JSONResponse

from apps.healthcheck.router import router


@router.get('/api/probes/readiness/')
async def readiness_probe():
    return JSONResponse(status_code=status.HTTP_200_OK, content={})
