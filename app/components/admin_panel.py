import reflex as rx
from app.states.contact_state import ContactState
from app.config import APIConfig


def admin_panel() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "API Configuration", class_name="text-xl font-bold text-gray-800 mb-4"
            ),
            rx.el.div(
                rx.el.label(
                    "Current Base URL:",
                    class_name="block text-sm font-medium text-gray-700 mb-2",
                ),
                rx.el.p(
                    APIConfig.BASE_URL,
                    class_name="text-sm text-gray-600 mb-4 p-2 bg-gray-100 rounded",
                ),
            ),
            rx.el.div(
                rx.el.label(
                    "Update Base URL:",
                    class_name="block text-sm font-medium text-gray-700 mb-2",
                ),
                rx.el.input(
                    placeholder="https://your-new-base-url.com",
                    on_change=ContactState.update_base_url.debounce(500),
                    class_name="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500",
                ),
            ),
            rx.cond(
                ContactState.api_success != "",
                rx.el.div(
                    ContactState.api_success,
                    class_name="mt-4 p-3 bg-green-100 border border-green-300 rounded-lg text-green-700 text-sm",
                ),
            ),
            class_name="bg-white p-6 rounded-lg shadow-lg border border-gray-200",
        ),
        class_name="max-w-md mx-auto mt-8",
    )