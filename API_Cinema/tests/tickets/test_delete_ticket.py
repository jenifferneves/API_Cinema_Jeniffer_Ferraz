import pytest
import json
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_delete_ticket_success():

    payload = {
        "movieId": "1LjOU2HC3p9Vm3AN",
        "seatNumber": 20,
        "price": 30,
        "showtime": "14:00"
    }

    async with async_playwright() as p:

        client = await p.request.new_context(base_url="http://localhost:3000")

        create_response = await client.post(
            "/tickets",
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

        assert create_response.status == 201

        tickets_response = await client.get("/tickets")
        tickets = await tickets_response.json()

        ticket_id = tickets[-1]["_id"]

        delete_response = await client.delete(f"/tickets/{ticket_id}")

        assert delete_response.status == 200