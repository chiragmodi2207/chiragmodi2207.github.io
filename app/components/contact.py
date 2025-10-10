import reflex as rx
from app.components.icons import map_pin_icon, phone_icon, mail_icon

def contact_form() -> rx.Component:
    script = """
const scriptURL = 'https://script.google.com/macros/s/AKfycbwGeKO4c9LQCM1NuczFV3MDP13iNLg0V1n1IFcsAc2EOeqMWlQZFdub0BcoyAzYwbXc/exec';
const form = document.getElementById('contact-form');

const attachListener = () => {
    const form = document.getElementById('contact-form');
    if (form && !form.dataset.listenerAttached) {
        form.addEventListener('submit', e => {
          e.preventDefault();

          const submitButton = form.querySelector('button[type="submit"]');
          const originalButtonHTML = submitButton.innerHTML;
          submitButton.disabled = true;

          const spinner = document.createElement('div');
          spinner.className = 'animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2';
          submitButton.innerHTML = '';
          submitButton.appendChild(spinner);
          submitButton.append('Sending...');

          fetch(scriptURL, { method: 'POST', body: new FormData(form)})
            .then(response => {
                if(response.ok) {
                    alert('Message sent successfully!');
                    form.reset();
                } else {
                    response.text().then(text => { 
                        console.error('Error!', text);
                        alert('Error sending message: ' + text);
                    })
                }
            })
            .catch(error => {
                console.error('Error!', error.message);
                alert('Error! ' + error.message);
            })
            .finally(() => {
                submitButton.disabled = false;
                submitButton.innerHTML = originalButtonHTML;
            });
        });
        form.dataset.listenerAttached = 'true';
    }
};

setTimeout(attachListener, 100);
"""

    return rx.el.div(
        # Heading
        rx.el.h2(
            "Get in Touch",
            class_name="font-['Roboto'] text-3xl md:text-4xl font-bold text-gray-900 tracking-tight text-center",
        ),
        rx.el.p(
            "Have questions? We're here to help. Reach out to us for a free consultation.",
            class_name="font-['Roboto'] max-w-xl mx-auto text-lg text-gray-600 mt-4 mb-12 text-center",
        ),

        # Contact details + form container
        rx.el.div(
            # Left: Contact Info + Map
            rx.el.div(
                rx.el.h3(
                    "Contact Information",
                    class_name="font-['Roboto'] text-xl font-bold text-gray-800 mb-6",
                ),
                rx.el.div(
                    map_pin_icon(class_name="w-6 h-6 text-emerald-600 mr-4 flex-shrink-0"),
                    rx.el.p(
                        "Kamlesh Taili and Associates,1699, Shivshakti society, Sokhda Road - Kheda ",
                        class_name="font-['Roboto'] text-gray-600",
                    ),
                    class_name="flex items-start mb-4",
                ),
                rx.el.div(
                    phone_icon(class_name="w-6 h-6 text-emerald-600 mr-4 flex-shrink-0"),
                    rx.el.p(
                        "+91 9033239113",
                        class_name="font-['Roboto'] text-gray-600",
                    ),
                    class_name="flex items-center mb-4",
                ),
                rx.el.div(
                    mail_icon(class_name="w-6 h-6 text-emerald-600 mr-4 flex-shrink-0"),
                    rx.el.p(
                        "kamlesh.taili@kntassociates.com",
                        class_name="font-['Roboto'] text-gray-600",
                    ),
                    class_name="flex items-center mb-4",
                ),
                rx.el.div(
                    rx.el.iframe(
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3719.0784313079945!2d72.685708!3d22.717798!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x395e7f8e0bd2c2ed%3A0x5b32fa3cfeb39fcb!2sSokhda%2C%20Gujarat%20387570!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin",
                        allowfullscreen=True,
                        loading="lazy",
                        referrerpolicy="no-referrer-when-downgrade",
                        class_name="w-full h-64 rounded-lg border-0 shadow-md",
                    )
                    ,
                    class_name="mt-6",
                ),
                class_name="w-full lg:w-1/3",
            ),

            # Right: Contact Form
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
                        class_name="font-['Roboto'] mt-1 block w-full px-4 py-3 bg-white border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-emerald-500 focus:border-emerald-500",
                    ),
                    class_name="mb-6",
                ),
                rx.el.button(
                    "Send Message",
                    type="submit",
                    class_name="font-['Roboto'] w-full inline-flex items-center justify-center bg-emerald-600 text-white px-6 py-3 rounded-lg text-base font-semibold shadow-lg hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 transition-all duration-300 disabled:bg-emerald-400",
                ),
                id="contact-form",
                class_name="w-full lg:w-2/3 bg-white p-8 rounded-2xl shadow-lg border border-gray-100",
            ),
            class_name="flex flex-col lg:flex-row gap-12 lg:gap-16",
        ),

        # Attach the script
        rx.script(script),

        id="contact",
        class_name="container mx-auto px-4 py-20",
    )
