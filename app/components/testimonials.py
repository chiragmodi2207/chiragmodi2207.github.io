import reflex as rx
from app.states.state import State


def testimonial_card(testimonial: dict) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            f'''"{testimonial['quote']}"''',
            class_name="font-['Roboto'] text-lg text-gray-700 italic mb-6",
        ),
        rx.el.div(
            rx.image(
                src=testimonial["avatar_url"],
                alt=testimonial["name"],
                class_name="w-12 h-12 rounded-full mr-4",
            ),
            rx.el.div(
                rx.el.p(
                    testimonial["name"],
                    class_name="font-['Roboto'] font-bold text-gray-900",
                ),
                rx.el.p(
                    testimonial["role"],
                    class_name="font-['Roboto'] text-sm text-gray-500",
                ),
            ),
            class_name="flex items-center",
        ),
        class_name="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 min-w-[300px] snap-center",
    )





def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "What Our Clients Say",
                class_name="font-['Roboto'] text-3xl md:text-4xl font-bold text-gray-900 tracking-tight text-center",
            ),
            rx.el.p(
                "Building relationships through exceptional service and results.",
                class_name="font-['Roboto'] max-w-xl mx-auto text-lg text-gray-600 mt-4 mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(State.testimonials, testimonial_card),
                class_name=(
                    "flex gap-6 overflow-x-auto snap-x snap-mandatory scroll-smooth "
                    "px-2 py-4 [-webkit-overflow-scrolling:_touch]"
                ),
            ),
            class_name="container mx-auto px-4 py-20",
        ),
        id="testimonials",
        class_name="bg-white",
    )




