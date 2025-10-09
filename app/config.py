import reflex as rx
from typing import Optional
import os


class APIConfig:
    """Configuration class for API settings."""

    BASE_URL: str = os.getenv(
        "API_BASE_URL", "https://modi2207.github.io/knt_associates_web_app"
    )
    ENDPOINTS = {
        "contact": "/api/contact",
        "services": "/api/services",
        "testimonials": "/api/testimonials",
        "team": "/api/team",
    }

    @classmethod
    def get_full_url(cls, endpoint_key: str) -> str:
        """Get the full URL for a given endpoint key."""
        endpoint = cls.ENDPOINTS.get(endpoint_key, "")
        return f"{cls.BASE_URL.rstrip('/')}{endpoint}"

    @classmethod
    def set_base_url(cls, base_url: str) -> None:
        """Dynamically change the base URL."""
        cls.BASE_URL = base_url.rstrip("/")