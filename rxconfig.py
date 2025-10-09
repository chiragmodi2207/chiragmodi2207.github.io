import reflex as rx
config = rx.Config(
    app_name="app",
    plugins=[rx.plugins.TailwindV3Plugin()],
    frontend_port=3000,
    backend_port=8000,
    deploy_url="https://modi2207.github.io/knt_associates_web_app/",
)