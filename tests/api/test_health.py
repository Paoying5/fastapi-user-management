def test_health(client):

    response = client.get(client.base_url + "/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["database"] == "connected"