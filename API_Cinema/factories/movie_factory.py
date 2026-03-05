import random


def valid_movie():
    return {
        "title": f"Filme Teste {random.randint(1,1000)}",
        "description": "Descrição teste",
        "launchdate": "2024-01-01",
        "showtimes": ["14:00"]
    }


def movie_without_title():
    return {
        "description": "Sem título",
        "launchdate": "2024-01-01",
        "showtimes": ["14:00"]
    }
