from tortoise import fields

from apps.common.models import TimestampMixin
from apps.common.utils.models import id_with_prefix


class Metric(TimestampMixin):
    id = fields.CharField(pk=True, max_length=27, default=id_with_prefix('m'))
    service_name = fields.CharField(max_length=255, index=True)
    path = fields.CharField(max_length=255)
    response_time_ms = fields.IntField()

    class Meta:
        table = 'metric'
