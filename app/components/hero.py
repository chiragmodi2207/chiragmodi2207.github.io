import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Expert Financial Guidance for Your Business Success",
                    class_name="font-['Roboto'] text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 tracking-tighter mb-6 text-center",
                ),
                rx.el.p(
                    "We provide comprehensive chartered accountancy services to help you navigate the complexities of finance with confidence and clarity.",
                    class_name="font-['Roboto'] max-w-2xl mx-auto text-lg md:text-xl text-gray-600 mb-10 text-center",
                ),
                rx.el.div(
                    rx.el.a(
                        "Our Services",
                        href="#services",
                        class_name="font-['Roboto'] inline-flex items-center justify-center bg-emerald-600 text-white px-8 py-3 rounded-lg text-base font-semibold shadow-lg hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition-all duration-300",
                    ),
                    rx.el.a(
                        "Contact Us",
                        href="#contact",
                        class_name="font-['Roboto'] inline-flex items-center justify-center bg-white text-emerald-600 px-8 py-3 rounded-lg text-base font-semibold border border-emerald-600 shadow-sm hover:bg-emerald-50 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition-all duration-300",
                    ),
                    class_name="flex flex-col sm:flex-row items-center justify-center gap-4",
                ),
                class_name="flex flex-col items-center",
            ),
            class_name="container mx-auto px-4 py-24 md:py-32",
        ),
        id="home",
        class_name="bg-gray-50",
    )