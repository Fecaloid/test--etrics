from unittest.mock import AsyncMock
from unittest.mock import patch

import pytest

from apps.healthcheck.enums import StatusEnum
from apps.healthcheck.serializers.healthcheck_result import HealthcheckResult
from apps.healthcheck.serializers.healthcheck_result import HealthcheckServiceResult


@pytest.mark.asyncio
async def test_liveness_probe_success(client):
    with patch('apps.healthcheck.controllers.liveness.healthchecker.healthcheck', AsyncMock()) as healthcheck_mock:
        healthcheck_mock.return_value = HealthcheckResult(
            status=StatusEnum.success,
            details=[HealthcheckServiceResult(status=StatusEnum.success, service='test')],
        )
        response = await client.get(client.app.url_path_for('liveness_probe'))

    assert 200 == response.status_code, response.text
    assert {
        'details': [
            {'message': '', 'service': 'test', 'status': 'success'},
        ],
        'status': 'success',
    } == response.json()
