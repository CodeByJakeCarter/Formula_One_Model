import time
import uuid

import pytest
import httpx

from f1model.main import app


@pytest.mark.anyio
async def test_driver_list() -> None:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url='http://test') as client:
        driver_ref_1 = f"test_driver_list_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}"
        driver_ref_2 = f"test_driver_list_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}"

        test_driver_1 = await client.post(
            '/api/v1/drivers/',
            json={
                'driver_ref': driver_ref_1,
                'first_name': 'Testy1',
                'last_name': 'Mctest1',
            },
        )
        test_driver_2 = await client.post(
            '/api/v1/drivers/',
            json={
                'driver_ref': driver_ref_2,
                'first_name': 'Testy2',
                'last_name': 'Mctest2',
            },
        )

        assert test_driver_1.status_code == 201
        assert test_driver_2.status_code == 201

        created_1 = test_driver_1.json()
        created_2 = test_driver_2.json()

        response = await client.get('/api/v1/drivers/')

    assert response.status_code == 200

    items = response.json()
    returned_ids = {item['id'] for item in items}

    assert created_1['id'] in returned_ids
    assert created_2['id'] in returned_ids
