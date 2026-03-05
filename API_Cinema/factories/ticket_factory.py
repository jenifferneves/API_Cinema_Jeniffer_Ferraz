def valid_ticket(movie_id):
    return {
        "movieId": movie_id,
        "seatNumber": 10,          # número
        "price": 30,               # número entre 0 e 60
        "showtime": "14:00"        # precisa bater com o filme
    }
