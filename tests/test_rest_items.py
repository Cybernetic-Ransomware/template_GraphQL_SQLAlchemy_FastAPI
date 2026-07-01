def test_create_item(client):
    response = client.post("/items/", json={"name": "widget"})

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "widget"
    assert "id" in body


def test_read_items_empty(client):
    response = client.get("/items/")

    assert response.status_code == 200
    assert response.json() == []


def test_read_items_after_create(client):
    client.post("/items/", json={"name": "widget"})

    response = client.get("/items/")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["name"] == "widget"


def test_read_item_by_id(client):
    created = client.post("/items/", json={"name": "widget"}).json()

    response = client.get(f"/item/{created['id']}")

    assert response.status_code == 200
    assert response.json()["name"] == "widget"


def test_read_item_not_found(client):
    response = client.get("/item/999")

    assert response.status_code == 404
