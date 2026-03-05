from utils.api_client import APIClient

client = APIClient("http://127.0.0.1:3000")


def create_ticket(payload):
    return client.post("/tickets", payload)

print("cheguei aqui")
def delete_ticket(ticket_id):
    return client.delete(f"/tickets/{ticket_id}")

