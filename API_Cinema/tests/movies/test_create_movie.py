import uuid
import json
from datetime import datetime, timedelta


def test_create_movie_success(api_context):
    movie_payload = {
        "title": f"Movie {uuid.uuid4()}",
        "description": "Test description",
        "launchdate": datetime.now().isoformat(),
        "showtimes": [
            (datetime.now() + timedelta(days=1)).isoformat(),
            (datetime.now() + timedelta(days=2)).isoformat()
        ]
    }

    response = api_context.post(
        "/movies",
        data=json.dumps(movie_payload),
        headers={"Content-Type": "application/json"}
    )

    print("STATUS:", response.status)
    print("BODY:", response.text())

    assert response.status == 201

    # Só valida body se ele existir
    if response.text():
        body = response.json()
        assert body["title"] == movie_payload["title"]


def test_create_movie_without_title(api_context):
    movie_payload = {
        "description": "No title movie",
        "launchdate": datetime.now().isoformat(),
        "showtimes": [
            (datetime.now() + timedelta(days=1)).isoformat()
        ]
    }

    response = api_context.post(
        "/movies",
        data=json.dumps(movie_payload),
        headers={"Content-Type": "application/json"}
    )

    print("STATUS:", response.status)
    print("BODY:", response.text())

    assert response.status == 400