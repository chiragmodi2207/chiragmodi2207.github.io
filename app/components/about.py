import reflex as rx
from app.states.state import State


def team_member_card(member: dict) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=member["avatar_url"],
            alt=member["name"],
            class_name="w-24 h-24 rounded-full mx-auto mb-4 border-4 border-white shadow-md",
        ),
        rx.el.h3(
            member["name"],
            class_name="font-['Roboto'] text-lg font-bold text-gray-900 text-center",
        ),
        rx.el.p(
            member["role"],
            class_name="font-['Roboto'] text-sm text-emerald-700 text-center",
        ),
        class_name="flex flex-col items-center",
    )


def about_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Your Trusted Financial Partners",
                    class_name="font-['Roboto'] text-3xl md:text-4xl font-bold text-gray-900 tracking-tight",
                ),
                rx.el.p(
                    "At Apex Accountants, we are a team of dedicated and experienced professionals committed to delivering exceptional financial services. Our mission is to empower our clients with the knowledge and support they need to achieve their financial goals. We believe in building long-term relationships based on trust, integrity, and a deep understanding of your unique needs.",
                    class_name="font-['Roboto'] text-lg text-gray-600 mt-6",
                ),
                class_name="max-w-3xl mb-12",
            ),
            rx.el.h3(
                "Meet Our Expert Team",
                class_name="font-['Roboto'] text-2xl font-bold text-gray-900 mb-8 text-center",
            ),
            rx.el.div(
                rx.foreach(State.team, team_member_card),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-8",
            ),
            class_name="container mx-auto px-4 py-20 flex flex-col items-center",
        ),
        id="about",
        class_name="bg-gray-50",
    )