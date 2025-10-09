import reflex as rx
from app.components.icons import trending_up_icon


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    trending_up_icon(class_name="text-emerald-500 h-7 w-7"),
                    rx.el.span(
                        "KNT Associates",
                        class_name="font-['Roboto'] text-lg font-bold text-gray-700 ml-2",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.p(
                    "Your partners in financial clarity and growth.",
                    class_name="font-['Roboto'] text-sm text-gray-500 mt-4",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Quick Links",
                        class_name="font-['Roboto'] text-sm font-semibold text-gray-800 tracking-wider uppercase",
                    ),
                    rx.el.a(
                        "Services",
                        href="#services",
                        class_name="mt-4 block text-base text-gray-500 hover:text-emerald-600",
                    ),
                    rx.el.a(
                        "About Us",
                        href="#about",
                        class_name="mt-3 block text-base text-gray-500 hover:text-emerald-600",
                    ),
                    rx.el.a(
                        "Contact",
                        href="#contact",
                        class_name="mt-3 block text-base text-gray-500 hover:text-emerald-600",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Follow Us",
                        class_name="font-['Roboto'] text-sm font-semibold text-gray-800 tracking-wider uppercase",
                    ),
                    rx.el.a(
                        "LinkedIn",
                        href="#",
                        class_name="mt-4 block text-base text-gray-500 hover:text-emerald-600",
                    ),
                    rx.el.a(
                        "Twitter",
                        href="#",
                        class_name="mt-3 block text-base text-gray-500 hover:text-emerald-600",
                    ),
                ),
                class_name="grid grid-cols-2 gap-8",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12",
        ),
        rx.el.div(
            rx.el.p(
                f"© 2025 KNT Associates. All rights reserved.",
                class_name="font-['Roboto'] text-sm text-gray-500",
            ),
            class_name="mt-12 pt-8 border-t border-gray-200 text-center",
        ),
        class_name="bg-gray-50 px-4 py-12",
    )