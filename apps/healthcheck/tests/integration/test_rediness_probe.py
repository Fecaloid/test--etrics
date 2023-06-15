import pytest


@pytest.mark.asyncio
async def test_readiness_probe_success(client):
    response = await client.get(client.app.url_path_for('readiness_probe'))

    assert 200 == response.status_code, response.text
    assert {} == response.json()
