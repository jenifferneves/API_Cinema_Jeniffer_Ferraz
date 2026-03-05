import json
from playwright.sync_api import sync_playwright


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, payload):
        with sync_playwright() as p:
            request = p.request.new_context(base_url=self.base_url)

            response = request.post(
                endpoint,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"}
            )

            try:
                body = response.json()
            except:
                body = None

            request.dispose()

            return {
                "status": response.status,
                "body": body
            }

    def get(self, endpoint):
        with sync_playwright() as p:
            request = p.request.new_context(base_url=self.base_url)

            response = request.get(endpoint)

            try:
                body = response.json()
            except:
                body = None

            request.dispose()

            return {
                "status": response.status,
                "body": body
            }

    def delete(self, endpoint):
        with sync_playwright() as p:
            request = p.request.new_context(base_url=self.base_url)

            response = request.delete(endpoint)

            try:
                body = response.json()
            except:
                body = None

            request.dispose()

            return {
                "status": response.status,
                "body": body
            }