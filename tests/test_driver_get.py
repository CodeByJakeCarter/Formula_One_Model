from fastapi.testclient import TestClient
from f1model.main import app
import time
import uuid


client = TestClient(app)

def test_driver_get():
    driver_ref = f"test_driver_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}"

    test_driver = client.post("/api/v1/drivers/", json={
        "driver_ref": driver_ref,
        "first_name": "Testy",
        "last_name": "Mctest"})
    assert test_driver.status_code == 201
    
    created = test_driver.json()
    created_id = created["id"]

    found = client.get("/api/v1/drivers/" + str(created_id))
    assert found.status_code == 200
    assert found.json()["id"] == created_id

    missing = client.get("/api/v1/drivers/" + "999")
    assert missing.status_code == 404
    assert missing.json() == {"detail": "Driver not found"}
    