import reflex as rx
import httpx
import logging
from typing import Any, Optional
from app.config import APIConfig


class APIState(rx.State):
    """State for handling API operations."""

    api_loading: bool = False
    api_error: str = ""
    api_success: str = ""

    @rx.event(background=True)
    async def make_api_request(
        self, endpoint_key: str, data: dict[str, Any], method: str = "POST"
    ):
        """Make an API request to the specified endpoint."""
        async with self:
            self.api_loading = True
            self.api_error = ""
            self.api_success = ""
        try:
            url = APIConfig.get_full_url(endpoint_key)
            async with httpx.AsyncClient() as client:
                if method.upper() == "POST":
                    response = await client.post(url, json=data)
                elif method.upper() == "GET":
                    response = await client.get(url, params=data)
                else:
                    response = await client.request(method, url, json=data)
                if response.status_code == 200:
                    async with self:
                        self.api_success = "Request completed successfully"
                        self.api_loading = False
                    return response.json()
                else:
                    async with self:
                        self.api_error = (
                            f"API Error: {response.status_code} - {response.text}"
                        )
                        self.api_loading = False
        except httpx.RequestError as e:
            logging.exception(f"API Request Error: {e}")
            async with self:
                self.api_error = f"Connection error: {str(e)}"
                self.api_loading = False
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            async with self:
                self.api_error = f"Unexpected error: {str(e)}"
                self.api_loading = False

    @rx.event
    def clear_api_messages(self):
        """Clear API status messages."""
        self.api_error = ""
        self.api_success = ""

    @rx.event
    def update_base_url(self, new_base_url: str):
        """Update the API base URL."""
        APIConfig.set_base_url(new_base_url)
        self.api_success = f"Base URL updated to: {new_base_url}"