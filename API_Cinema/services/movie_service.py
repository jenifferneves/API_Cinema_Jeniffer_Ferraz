from utils.api_client import APIClient

client = APIClient("http://127.0.0.1:3000")

def create_movie(payload):
    return client.post("/movies", payload)

def delete_movie(movie_id):
    return client.delete(f"/movies/{movie_id}")

def get_movies():
    return client.get("/movies")
