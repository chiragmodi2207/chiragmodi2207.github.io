import reflex as rx


def trending_up_icon(class_name: str) -> rx.Component:
    return rx.el.svg(
        rx.el.svg.polyline(points="22 7 13.5 15.5 8.5 10.5 2 17"),
        rx.el.svg.polyline(points="16 7 22 7 22 13"),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        class_name=class_name,
    )


def map_pin_icon(class_name: str) -> rx.Component:
    return rx.el.svg(
        rx.el.svg.path(d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"),
        rx.el.svg.circle(cx="12", cy="10", r="3"),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        class_name=class_name,
    )


def phone_icon(class_name: str) -> rx.Component:
    return rx.el.svg(
        rx.el.svg.path(
            d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
        ),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        class_name=class_name,
    )


def mail_icon(class_name: str) -> rx.Component:
    return rx.el.svg(
        rx.el.svg.rect(width="20", height="16", x="2", y="4", rx="2"),
        rx.el.svg.path(d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        class_name=class_name,
    )


def landmark_icon(class_name: str) -> rx.Component:
    return rx.el.svg(
        rx.el.svg.path(d="M3 22h18"),
        rx.el.svg.path(d="M5 22V8l7-5 7 5v14"),
        rx.el.svg.path(d="M12 22V10"),
        rx.el.svg.path(d="M12 10l5 2"),
        rx.el.svg.path(d="M12 10l-5 2"),
        rx.el.svg.path(d="M17 10l-5-2"),
        rx.el.svg.path(d="M7 10l5-2"),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        class_name=class_name,
    )


def globe_icon(class_name: str) -> rx.Component:
    return rx.el.svg(
        rx.el.svg.circle(cx="12", cy="12", r="10"),
        rx.el.svg.path(d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"),
        rx.el.svg.path(d="M2 12h20"),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        class_name=class_name,
    )


def check_check_icon(class_name: str) -> rx.Component:
    return rx.el.svg(
        rx.el.svg.path(d="M18 6 7 17l-5-5"),
        rx.el.svg.path(d="m22 10-7.5 7.5L13 16"),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        class_name=class_name,
    )