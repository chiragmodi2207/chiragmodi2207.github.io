import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.services import services_section
from app.components.about import about_section
from app.components.testimonials import testimonials_section
from app.components.contact import contact_form
from app.components.footer import footer
from app.components.admin_panel import admin_panel
from app.states.state import State


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero(),
        services_section(),
        about_section(),
        testimonials_section(),
        contact_form(),
        footer(),
        class_name="font-['Roboto'] bg-white",
    )


def admin() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.h1("Admin Panel", class_name="text-3xl font-bold text-center mb-8"),
            admin_panel(),
            class_name="container mx-auto px-4 py-12",
        ),
        class_name="font-['Roboto'] bg-gray-50 min-h-screen",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Apex Accountants | Expert Financial Guidance")
app.add_page(admin, route="/admin", title="Admin Panel - Apex Accountants")