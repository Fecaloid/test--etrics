import factory

from apps.common.tests.async_factory import AsyncFactory
from apps.metric.models import Metric


class MetricFactory(AsyncFactory):
    service_name = factory.Sequence(lambda n: f'service_name_{n}')
    path = factory.Sequence(lambda n: f'path_{n}')
    response_time_ms = factory.Sequence(lambda n: n)

    class Meta:
        model = Metric
