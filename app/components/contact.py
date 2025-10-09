import reflex as rx
from app.components.icons import map_pin_icon, phone_icon, mail_icon
from app.states.contact_state import ContactState


def contact_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Get in Touch",
            class_name="font-['Roboto'] text-3xl md:text-4xl font-bold text-gray-900 tracking-tight text-center",
        ),
        rx.el.p(
            "Have questions? We're here to help. Reach out to us for a free consultation.",
            class_name="font-['Roboto'] max-w-xl mx-auto text-lg text-gray-600 mt-4 mb-12 text-center",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Contact Information",
                    class_name="font-['Roboto'] text-xl font-bold text-gray-800 mb-6",
                ),
                rx.el.div(
                    map_pin_icon(
                        class_name="w-6 h-6 text-emerald-600 mr-4 flex-shrink-0"
                    ),
                    rx.el.p(
                        "123 Finance Street, Suite 400, Capital City, 12345",
                        class_name="font-['Roboto'] text-gray-600",
                    ),
                    class_name="flex items-start mb-4",
                ),
                rx.el.div(
                    phone_icon(
                        class_name="w-6 h-6 text-emerald-600 mr-4 flex-shrink-0"
                    ),
                    rx.el.p(
                        "(123) 456-7890", class_name="font-['Roboto'] text-gray-600"
                    ),
                    class_name="flex items-center mb-4",
                ),
                rx.el.div(
                    mail_icon(class_name="w-6 h-6 text-emerald-600 mr-4 flex-shrink-0"),
                    rx.el.p(
                        "contact@apexaccountants.com",
                        class_name="font-['Roboto'] text-gray-600",
                    ),
                    class_name="flex items-center mb-4",
                ),
                class_name="w-full lg:w-1/3",
            ),
            rx.el.div(
                rx.cond(
                    ContactState.api_error != "",
                    rx.el.div(
                        rx.el.p(
                            ContactState.api_error,
                            class_name="font-['Roboto'] text-red-600 text-sm",
                        ),
                        class_name="mb-4 p-3 bg-red-100 border border-red-300 rounded-lg",
                    ),
                ),
                rx.cond(
                    ContactState.api_success != "",
                    rx.el.div(
                        rx.el.p(
                            ContactState.api_success,
                            class_name="font-['Roboto'] text-green-600 text-sm",
                        ),
                        class_name="mb-4 p-3 bg-green-100 border border-green-300 rounded-lg",
                    ),
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Full Name",
                            html_for="name",
                            class_name="font-['Roboto'] block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="name",
                            id="name",
                            placeholder="Your Name",
                            required=True,
                            default_value=ContactState.contact_name,
                            key=ContactState.contact_name,
                            class_name="font-['Roboto'] mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-emerald-500 focus:border-emerald-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email Address",
                            html_for="email",
                            class_name="font-['Roboto'] block text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="email",
                            id="email",
                            type="email",
                            placeholder="you@example.com",
                            required=True,
                            default_value=ContactState.contact_email,
                            key=ContactState.contact_email,
                            class_name="font-['Roboto'] mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-emerald-500 focus:border-emerald-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Message",
                            html_for="message",
                            class_name="font-['Roboto'] block text-sm font-medium text-gray-700",
                        ),
                        rx.el.textarea(
                            name="message",
                            id="message",
                            placeholder="How can we help you?",
                            required=True,
                            rows=4,
                            default_value=ContactState.contact_message,
                            key=ContactState.contact_message,
                            class_name="font-['Roboto'] mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-emerald-500 focus:border-emerald-500",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.button(
                        rx.cond(
                            ContactState.api_loading,
                            rx.el.div(
                                rx.el.div(
                                    class_name="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"
                                ),
                                "Sending...",
                                class_name="flex items-center justify-center",
                            ),
                            "Send Message",
                        ),
                        type="submit",
                        disabled=ContactState.api_loading,
                        class_name=rx.cond(
                            ContactState.api_loading,
                            "font-['Roboto'] w-full inline-flex items-center justify-center bg-emerald-400 text-white px-6 py-3 rounded-lg text-base font-semibold shadow-lg cursor-not-allowed",
                            "font-['Roboto'] w-full inline-flex items-center justify-center bg-emerald-600 text-white px-6 py-3 rounded-lg text-base font-semibold shadow-lg hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition-all duration-300",
                        ),
                    ),
                    on_submit=[
                        ContactState.submit_contact_form,
                        ContactState.clear_api_messages,
                    ],
                    reset_on_submit=True,
                ),
                class_name="w-full lg:w-2/3 bg-white p-8 rounded-2xl shadow-lg border border-gray-100",
            ),
            class_name="flex flex-col lg:flex-row gap-12 lg:gap-16",
        ),
        id="contact",
        class_name="container mx-auto px-4 py-20",
    )