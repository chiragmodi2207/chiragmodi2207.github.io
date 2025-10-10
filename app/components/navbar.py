import reflex as rx
from app.components.icons import trending_up_icon


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                trending_up_icon(class_name="text-emerald-600 h-8 w-8"),
                rx.el.span(
                    "KNT Associates",
                    class_name="font-['Roboto'] text-xl font-bold text-gray-800 ml-2",
                ),
                class_name="flex items-center",
            ),
            rx.el.nav(
                rx.el.a(
                    "Home",
                    href="#home",
                    class_name="font-['Roboto'] text-sm font-medium text-gray-600 hover:text-emerald-600 transition-colors",
                ),
                rx.el.a(
                    "Services",
                    href="#services",
                    class_name="font-['Roboto'] text-sm font-medium text-gray-600 hover:text-emerald-600 transition-colors",
                ),
                rx.el.a(
                    "Team",
                    href="#about",
                    class_name="font-['Roboto'] text-sm font-medium text-gray-600 hover:text-emerald-600 transition-colors",
                ),
                rx.el.a(
                    "Testimonials",
                    href="#testimonials",
                    class_name="font-['Roboto'] text-sm font-medium text-gray-600 hover:text-emerald-600 transition-colors",
                ),
                rx.el.a(
                    "Contact us",
                    href="#contact",
                    class_name="font-['Roboto'] text-sm font-medium text-gray-600 hover:text-emerald-600 transition-colors",
                ),
                # rx.el.a(
                #     "About us",
                #     href="#about",
                #     class_name="font-['Roboto'] text-sm font-medium text-gray-600 hover:text-emerald-600 transition-colors",
                # ),
                # rx.el.a(
                #     "Careers",
                #     href="#",
                #     class_name="font-['Roboto'] text-sm font-medium text-gray-600 hover:text-emerald-600 transition-colors",
                # ),
                class_name="hidden md:flex items-center gap-6",
            ),
            rx.el.a(
                "Get a Quote",
                href="#contact",
                class_name="font-['Roboto'] hidden sm:inline-flex items-center justify-center bg-emerald-600 text-white px-5 py-2.5 rounded-lg text-sm font-semibold shadow-md hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition-all duration-300",
            ),
            class_name="container mx-auto flex items-center justify-between h-16 px-4",
        ),
        class_name="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-gray-200",
    )