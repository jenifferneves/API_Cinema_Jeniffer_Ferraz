from services.movies_service import create_movie
from factories.movie_factory import movie_without_title

def test_create_movie_without_title():
    payload = movie_without_title()
    response = create_movie(payload)

    assert response["status"] == 400
