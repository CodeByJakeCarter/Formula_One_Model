import time
import uuid

import pytest
import httpx

from f1model.main import app


@pytest.mark.anyio
async def test_driver_get() -> None:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url='http://test') as client:
        driver_ref = f"test_driver_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}"

        test_driver = await client.post(
            '/api/v1/drivers/',
            json={
                'driver_ref': driver_ref,
                'first_name': 'Testy',
                'last_name': 'Mctest',
            },
        )
        assert test_driver.status_code == 201

        created_id = test_driver.json()['id']

        found = await client.get('/api/v1/drivers/' + str(created_id))
        assert found.status_code == 200
        assert found.json()['id'] == created_id

        missing = await client.get('/api/v1/drivers/999')
        assert missing.status_code == 404
        assert missing.json() == {'detail': 'Driver not found'}
