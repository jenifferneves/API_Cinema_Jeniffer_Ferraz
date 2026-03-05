import uuid
import json
from datetime import datetime, timedelta


def test_get_movie_by_id_success(api_context):
    movie_payload = {
        "title": f"Movie {uuid.uuid4()}",
        "description": "Get test",
        "launchdate": datetime.now().isoformat(),
        "showtimes": [
            (datetime.now() + timedelta(days=1)).isoformat()
        ]
    }

    # Criar filme
    create_response = api_context.post(
        "/movies",
        data=json.dumps(movie_payload),
        headers={"Content-Type": "application/json"}
    )

    assert create_response.status == 201

    # Buscar todos os filmes
    list_response = api_context.get("/movies")
    assert list_response.status == 200

    movies = list_response.json()

    # Procurar o filme pelo título
    created_movie = next(
        (movie for movie in movies if movie["title"] == movie_payload["title"]),
        None
    )

    assert created_movie is not None, "Filme criado não foi encontrado na lista"

    movie_id = created_movie["_id"]

    # Buscar por ID
    get_response = api_context.get(f"/movies/{movie_id}")
    assert get_response.status == 200

    movie = get_response.json()

    assert movie["_id"] == movie_id
    assert movie["title"] == movie_payload["title"]


def test_get_movie_not_found(api_context):
    response = api_context.get("/movies/invalid-id")

    assert response.status == 404