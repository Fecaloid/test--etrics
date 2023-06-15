from apps.healthcheck.enums import StatusEnum
from apps.healthcheck.models import TestModel
from apps.healthcheck.serializers.healthcheck_result import HealthcheckServiceResult
from apps.healthcheck.services.checkers.base import BaseHealthchecker


class DBHealthchecker(BaseHealthchecker):
    async def check(self) -> HealthcheckServiceResult:
        try:
            obj = await TestModel.create(title='test')
            obj.title = 'newtest'
            await obj.save()
            await obj.delete()

            return HealthcheckServiceResult(status=StatusEnum.success, service='db')
        except Exception as e:
            return HealthcheckServiceResult(status=StatusEnum.error, service='db', message=str(e))
