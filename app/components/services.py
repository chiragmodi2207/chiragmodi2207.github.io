import reflex as rx
from app.states.state import State
from app.components.icons import check_check_icon, landmark_icon, globe_icon


def service_item(service: dict) -> rx.Component:
    return rx.el.li(
        check_check_icon(class_name="w-5 h-5 text-emerald-500 mr-3 flex-shrink-0 mt-1"),
        rx.el.div(
            rx.el.h4(
                service["name"],
                class_name="font-['Roboto'] text-base font-semibold text-gray-800",
            ),
            rx.el.p(
                service["description"],
                class_name="font-['Roboto'] text-sm text-gray-600",
            ),
        ),
        class_name="flex items-start",
    )


def service_category_card(category: dict) -> rx.Component:
    icon_map = {"landmark": landmark_icon, "globe": globe_icon}
    icon_func = icon_map.get(category["icon"], landmark_icon)
    return rx.el.div(
        rx.el.div(
            icon_func(class_name="w-10 h-10 text-emerald-600"),
            class_name="p-4 bg-emerald-100 rounded-xl mb-6 w-fit",
        ),
        rx.el.h3(
            category["title"],
            class_name="font-['Roboto'] text-2xl font-bold text-gray-900 mb-4",
        ),
        rx.el.p(
            category["description"],
            class_name="font-['Roboto'] text-base text-gray-600 mb-6",
        ),
        rx.el.ul(rx.foreach(category["items"], service_item), class_name="space-y-4"),
        class_name="bg-white p-8 rounded-2xl shadow-sm hover:shadow-lg border border-gray-100 transition-all duration-300 hover:-translate-y-1",
    )


def services_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Our Comprehensive Services",
                    class_name="font-['Roboto'] text-3xl md:text-4xl font-bold text-gray-900 tracking-tight text-center",
                ),
                rx.el.p(
                    "Tailored financial solutions for UK and Indian markets.",
                    class_name="font-['Roboto'] max-w-xl mx-auto text-lg text-gray-600 mt-4 text-center",
                ),
                class_name="mb-12",
            ),
            rx.el.div(
                rx.foreach(State.services, service_category_card),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
            ),
            class_name="container mx-auto px-4 py-20",
        ),
        id="services",
        class_name="bg-gray-50",
    )