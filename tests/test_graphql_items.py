def _create_item(client, name: str) -> int:
    mutation = f'mutation {{ createItem(name: "{name}") {{ id }} }}'
    response = client.post("/graphql", json={"query": mutation})
    return response.json()["data"]["createItem"]["id"]


def test_create_item(client):
    response = client.post("/graphql", json={"query": 'mutation { createItem(name: "widget") { id name } }'})

    assert response.status_code == 200
    data = response.json()["data"]["createItem"]
    assert data["name"] == "widget"
    assert "id" in data


def test_items_query(client):
    _create_item(client, "widget")

    response = client.post("/graphql", json={"query": "query { items { id name } }"})

    assert response.status_code == 200
    items = response.json()["data"]["items"]
    assert len(items) == 1
    assert items[0]["name"] == "widget"


def test_item_query_by_id(client):
    item_id = _create_item(client, "widget")

    response = client.post("/graphql", json={"query": f"query {{ item(itemId: {item_id}) {{ id name }} }}"})

    assert response.status_code == 200
    assert response.json()["data"]["item"]["name"] == "widget"


def test_item_query_not_found(client):
    response = client.post("/graphql", json={"query": "query { item(itemId: 999) { id name } }"})

    assert response.status_code == 200
    assert response.json()["data"] is None
    assert response.json()["errors"]
