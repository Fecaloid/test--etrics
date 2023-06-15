import pytest
from fastapi import status

from apps.metric.models import Metric
from apps.metric.tests.factories import MetricFactory


async def set_data_to_db():
    data = [
        {'service_name': 'service_1', 'path': 'path_1', 'response_time_ms': 50},
        {'service_name': 'service_1', 'path': 'path_2', 'response_time_ms': 60},
        {'service_name': 'service_1', 'path': 'path_3', 'response_time_ms': 70},
        {'service_name': 'service_1', 'path': 'path_1', 'response_time_ms': 80},
        {'service_name': 'service_1', 'path': 'path_2', 'response_time_ms': 90},
        {'service_name': 'service_1', 'path': 'path_3', 'response_time_ms': 100},
        {'service_name': 'service_1', 'path': 'path_1', 'response_time_ms': 110},
        {'service_name': 'service_1', 'path': 'path_2', 'response_time_ms': 120},
        {'service_name': 'service_1', 'path': 'path_3', 'response_time_ms': 130},
        {'service_name': 'service_2', 'path': 'path_1', 'response_time_ms': 80},
        {'service_name': 'service_2', 'path': 'path_2', 'response_time_ms': 90},
        {'service_name': 'service_2', 'path': 'path_1', 'response_time_ms': 100},
    ]

    [await MetricFactory.create(**item) for item in data]


@pytest.mark.asyncio
async def test_set_metric(client):
    metric = await MetricFactory.build()
    request_data = {
        'service_name': metric.service_name,
        'path': metric.path,
        'response_time_ms': metric.response_time_ms,
    }

    response = await client.post('/api/metric/', params=request_data)

    assert status.HTTP_200_OK == response.status_code

    data = response.json()

    assert data['path'] == metric.path
    assert await Metric.all().count() == 1


@pytest.mark.asyncio
async def test_get_metric_service_1(client):
    await set_data_to_db()
    service_name = 'service_1'

    response = await client.get(f'/api/metric/{service_name}')

    assert status.HTTP_200_OK == response.status_code

    data = response.json()

    assert await Metric.all().count() == 12
    assert data['count'] == 3
    assert data['items'][0]['path'] == 'path_1'
    assert data['items'][0]['min_time'] == 50
    assert data['items'][0]['max_time'] == 110
    assert data['items'][0]['avg_time'] == 80
    assert data['items'][0]['p99'] == 66.67


@pytest.mark.asyncio
async def test_get_metric_service_2(client):
    await set_data_to_db()
    service_name = 'service_2'

    response = await client.get(f'/api/metric/{service_name}')

    assert status.HTTP_200_OK == response.status_code

    data = response.json()

    assert await Metric.all().count() == 12
    assert data['count'] == 2
    assert data['items'][0]['path'] == 'path_1'
    assert data['items'][0]['min_time'] == 80
    assert data['items'][0]['max_time'] == 100
    assert data['items'][0]['avg_time'] == 90
    assert data['items'][0]['p99'] == 50.0
