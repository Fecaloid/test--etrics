from fastapi import Depends
from tortoise.functions import Avg
from tortoise.functions import Count
from tortoise.functions import Max
from tortoise.functions import Min

from apps.metric.models import Metric
from apps.metric.router import router
from apps.metric.serializers.metric import MetricRequestSerializer
from apps.metric.serializers.metric import MetricResponseSerializer
from apps.metric.serializers.metric import MetricStatisticResponseSerializer
from apps.metric.serializers.metric import MetricStatisticSerializer
from config.constants import P99_DEFAULT_VALUE


@router.post('/api/metric/', response_model=MetricResponseSerializer)
async def set_metric(params: MetricRequestSerializer = Depends()):
    metric = await Metric.create(**params.dict())
    return MetricResponseSerializer.from_orm(metric)


@router.get('/api/metric/{service_name}', response_model=MetricStatisticResponseSerializer)
async def get_metric_statistic(service_name: str):
    metrics = (
        await Metric.filter(service_name=service_name)
        .annotate(
            count=Count('response_time_ms', 'count'),
            min_time=Min('response_time_ms', 'min_time'),
            max_time=Max('response_time_ms', 'max_time'),
            avg_time=Avg('response_time_ms', 'avg_time'),
        )
        .group_by('path')
        .values('count', 'min_time', 'max_time', 'avg_time', 'path')
    )

    percentage_data = (
        await Metric.filter(service_name=service_name, response_time_ms__lte=P99_DEFAULT_VALUE)
        .annotate(count=Count('response_time_ms', 'count'))
        .group_by('path')
        .values('count', 'path')
    )

    p99_count = {item['path']: item['count'] for item in percentage_data}

    response = []
    for item in metrics:
        p99 = round(p99_count[item['path']] / item['count'] * 100, 2)
        response.append(MetricStatisticSerializer(**item, p99=p99))

    return MetricStatisticResponseSerializer(count=len(metrics), items=response)
