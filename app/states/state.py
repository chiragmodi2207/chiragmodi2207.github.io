import reflex as rx
from typing import TypedDict


class ServiceItem(TypedDict):
    name: str
    description: str


class ServiceCategory(TypedDict):
    icon: str
    title: str
    description: str
    items: list[ServiceItem]


class Testimonial(TypedDict):
    name: str
    role: str
    quote: str
    avatar_url: str


class TeamMember(TypedDict):
    name: str
    role: str
    avatar_url: str


class State(rx.State):
    """The main state for the Chartered Accountant website."""

    is_submitting: bool = False
    services: list[ServiceCategory] = [
        {
            "icon": "landmark",
            "title": "UK Accounting",
            "description": "Comprehensive accounting services for UK-based businesses, ensuring compliance and efficiency. Our team helps you navigate the complexities of UK tax laws, from day-to-day bookkeeping to annual statutory filings.",
            "items": [
                {
                    "name": "Bookkeeping",
                    "description": "Meticulous record-keeping to ensure your financial data is accurate and up-to-date.",
                },
                {
                    "name": "VAT Return",
                    "description": "Timely and accurate VAT return submissions to keep you compliant with HMRC regulations.",
                },
                {
                    "name": "Self Assessment",
                    "description": "Hassle-free self-assessment tax return services for individuals and sole traders.",
                },
                {
                    "name": "Annual Account",
                    "description": "Preparation and submission of annual accounts for limited companies, ensuring statutory compliance.",
                },
            ],
        },
        {
            "icon": "globe",
            "title": "Indian Accounting",
            "description": "Expert financial services tailored to the Indian market, covering all statutory requirements. We provide end-to-end solutions for individuals and businesses, ensuring accurate tax filing and compliance with the latest regulations.",
            "items": [
                {
                    "name": "Income Tax Return",
                    "description": "Filing of income tax returns for individuals, HUFs, and businesses as per Indian tax laws.",
                },
                {
                    "name": "GST Return",
                    "description": "Complete GST compliance, from registration to monthly and annual return filings.",
                },
                {
                    "name": "Accounting",
                    "description": "Full-service accounting solutions for Indian businesses to maintain clean and compliant books.",
                },
                {
                    "name": "Audit",
                    "description": "Statutory and internal audit services to ensure financial accuracy and regulatory adherence.",
                },
            ],
        },
    ]
    testimonials = [
            {
                "name": "John Doe",
                "role": "CEO, Tech Innovators",
                "quote": "Their expertise in financial consulting was pivotal for our company's growth. Truly a game-changer.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=John",
            },
            {
                "name": "Jane Smith",
                "role": "Founder, Creative Co.",
                "quote": "The most professional and responsive accounting team I've ever worked with. They make tax season stress-free.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Jane",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
            {
                "name": "Samuel Green",
                "role": "Director, BuildRight",
                "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
                "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
            },
        ]
    active_testimonial: int = 0  # Current visible index


    def next_slide(self):
        if self.active_testimonial < self.testimonials.length() - 1:
            self.active_testimonial += 1

    def prev_slide(self):
        if self.active_testimonial > 0:
            self.active_testimonial -= 1

    def go_to_slide(self, index: int):
        self.active_testimonial = index

    def get_active_testimonial(self) -> int:
        return self.active_testimonial

    # testimonials: list[Testimonial] = [
    #     {
    #         "name": "John Doe",
    #         "role": "CEO, Tech Innovators",
    #         "quote": "Their expertise in financial consulting was pivotal for our company's growth. Truly a game-changer.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=John",
    #     },
    #     {
    #         "name": "Jane Smith",
    #         "role": "Founder, Creative Co.",
    #         "quote": "The most professional and responsive accounting team I've ever worked with. They make tax season stress-free.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Jane",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },
    #     {
    #         "name": "Samuel Green",
    #         "role": "Director, BuildRight",
    #         "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.",
    #         "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel",
    #     },

    # ]
    team: list[TeamMember] = [
        {
            "name": "Eleanor Vance",
            "role": "Managing Partner, CPA",
            "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=EleanorVance",
        },
        {
            "name": "Marcus Thorne",
            "role": "Senior Tax Consultant",
            "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=MarcusThorne",
        },
        {
            "name": "Isabelle Reed",
            "role": "Lead Auditor",
            "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=IsabelleReed",
        },
        {
            "name": "Julian Knox",
            "role": "Business Advisor",
            "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=JulianKnox",
        },
    ]