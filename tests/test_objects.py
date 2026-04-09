def test_list_objects_returns_seeded_objects(client):
    response = client.get("/api/v1/objects")
    payload = response.get_json()

    assert response.status_code == 200
    assert len(payload) == 2
    assert payload[0]["name"] == "Anemometer"


def test_get_unknown_object_returns_404(client):
    response = client.get("/api/v1/objects/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Object not found"}


def test_create_object_returns_created_payload(client):
    response = client.post(
        "/api/v1/objects",
        json={"name": "Thermometer", "description": "Temperature sensor"},
    )
    payload = response.get_json()

    assert response.status_code == 201
    assert payload["id"] == 3
    assert payload["name"] == "Thermometer"
