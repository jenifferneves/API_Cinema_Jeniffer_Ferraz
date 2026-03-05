from services.movies_service import create_movie, get_movies
from services.tickets_service import create_ticket, delete_ticket
from factories.movie_factory import valid_movie
from factories.ticket_factory import valid_ticket


def test_full_movie_ticket_flow():
    # Criar filme
    movie_payload = valid_movie()
    movie_response = create_movie(movie_payload)
    assert movie_response["status"] == 201

    # Buscar filmes para pegar o ID
    movies_response = get_movies()
    assert movies_response["status"] == 200

    movies = movies_response["body"]

    movie_title = movie_payload["title"]

    movie_id = next(
        movie["_id"]
        for movie in movies
        if movie["title"] == movie_title
    )

    # Criar ticket
    ticket_payload = valid_ticket(movie_id)
    ticket_response = create_ticket(ticket_payload)
    print("TICKET RESPONSE:", ticket_response)
    assert ticket_response["status"] == 201

    ticket_id = ticket_response["body"]["_id"]

    # Deletar ticket
    delete_response = delete_ticket(ticket_id)
    assert delete_response["status"] == 200
    
