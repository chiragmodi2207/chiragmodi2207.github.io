import reflex as rx
from app.states.api_state import APIState


class ContactState(APIState):
    """State for handling contact form submissions."""

    contact_name: str = ""
    contact_email: str = ""
    contact_message: str = ""

    @rx.event
    async def submit_contact_form(self, form_data: dict):
        """Submit contact form via API."""
        contact_data = {
            "name": form_data.get("name", ""),
            "email": form_data.get("email", ""),
            "message": form_data.get("message", ""),
            "timestamp": rx.State.router.page.path,
        }
        await self.make_api_request("contact", contact_data, "POST")
        if not self.api_error:
            self.contact_name = ""
            self.contact_email = ""
            self.contact_message = ""