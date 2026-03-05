import pytest
import uuid
import json
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_create_ticket_success():

    ticket_payload = {
        "movieId": "1LjOU2HC3p9Vm3AN",
        "seatNumber": 10,
        "price": 30,
        "showtime": "14:00"
    }

    async with async_playwright() as p:

        client = await p.request.new_context(base_url="http://localhost:3000")

        response = await client.post(
            "/tickets",
            data=json.dumps(ticket_payload),
            headers={"Content-Type": "application/json"}
        )

        print("STATUS:", response.status)
        print("BODY:", await response.text())

        assert response.status == 201