import pytest
import uuid
import json
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_update_movie_success():

    movie_payload = {
        "title": f"Movie {uuid.uuid4()}",
        "description": "Original description",
        "launchdate": "2025-01-01",
        "showtimes": ["14:00"]
    }

    async with async_playwright() as p:

        client = await p.request.new_context(base_url="http://localhost:3000")

        # Criar filme
        create_response = await client.post(
            "/movies",
            data=json.dumps(movie_payload),
            headers={"Content-Type": "application/json"}
        )

        assert create_response.status == 201

        # Buscar lista de filmes para pegar o ID
        movies_response = await client.get("/movies")
        movies = await movies_response.json()

        movie_id = movies[-1]["_id"]

        # Payload atualizado
        update_payload = {
            "title": "Movie Updated",
            "description": "Updated description",
            "launchdate": "2025-01-02",
            "showtimes": ["16:00"]
        }

        # Atualizar filme
        update_response = await client.put(
            f"/movies/{movie_id}",
            data=json.dumps(update_payload),
            headers={"Content-Type": "application/json"}
        )

        assert update_response.status == 200

        updated_movie = await update_response.json()

        assert updated_movie["title"] == "Movie Updated"
        assert updated_movie["description"] == "Updated description"