import pytest
import uuid
from playwright.sync_api import sync_playwright


def test_delete_movie_success():

    movie_payload = {
        "title": f"Movie {uuid.uuid4()}",
        "description": "Delete test",
        "launchdate": "2025-01-01",
        "showtimes": ["14:00"]
    }

    with sync_playwright() as p:

        client = p.request.new_context(base_url="http://localhost:3000")

        # Criar filme
        create_response = client.post("/movies", data=movie_payload)

        assert create_response.status == 201

        # Buscar filmes
        list_response = client.get("/movies")

        movies = list_response.json()
        movie_id = movies[-1]["_id"]

        # Deletar filme
        delete_response = client.delete(f"/movies/{movie_id}")

        assert delete_response.status == 200