"""
Usage:
    python manage.py seed_projects          # insert (skip if slug exists)
    python manage.py seed_projects --clear  # wipe and re-insert
"""

from django.core.management.base import BaseCommand

from portfolio.models import Project, TechStackItem, ProjectImage


PROJECTS = [
    {
        "slug": "rating-ranch",
        "name": "RatingRanch.com",
        "url": "https://ratingranch.com",
        "github_url": "",
        "description": (
            "Sports ratings platform featuring data import via Excel spreadsheets, "
            "Pandas-powered analytics, and public leaderboards. Built for the Alliance "
            "Sports organisation to manage and publish competitive ratings across multiple "
            "divisions."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 1,
        "tech_stack": [
            "Python", "Django", "PostgreSQL", "Pandas", "OpenPyXL", "FastAPI", "httpx",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/rating-ranch/screenshot.png",
                "image_type": "hero",
                "caption": "",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
        ],
    },
    {
        "slug": "breaking-news-guys",
        "name": "BreakingNewsGuys.com",
        "url": "https://breakingnewsguys.com",
        "github_url": "",
        "description": (
            "ASGI broadcast management system for a news team. Editors compose messages "
            "and dispatch them simultaneously to Discord webhooks and Slack via Bot Token "
            "API, with media uploads handled through Cloudinary."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 2,
        "tech_stack": [
            "Python", "Django", "PostgreSQL", "ASGI", "Cloudinary", "FastAPI",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/breaking-news/screenshot.png",
                "image_type": "hero",
                "caption": "",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/breaking-news/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
        ],
    },
    {
        "slug": "la-surfing-school",
        "name": "LAsurfing.school",
        "url": "https://lasurfing.school",
        "github_url": "",
        "description": (
            "Marketing and lesson-booking website for a Los Angeles surf instructor. "
            "Integrates Stripe for payment processing and Resend for transactional "
            "booking confirmation emails."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 3,
        "tech_stack": [
            "Python", "Django", "PostgreSQL", "Stripe", "Resend",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/la-surfing-school/screenshot.png",
                "image_type": "hero",
                "caption": "",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/la-surfing-school/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the database with initial portfolio projects"

    def add_arguments(self, parser):
        parser.add_argument("--clear", action="store_true", help="Delete all projects before seeding")

    def handle(self, *args, **options):
        if options["clear"]:
            Project.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared all projects."))

        for data in PROJECTS:
            tech = data.pop("tech_stack")
            images = data.pop("images")

            project, created = Project.objects.get_or_create(
                slug=data["slug"], defaults=data
            )

            if created:
                for i, name in enumerate(tech):
                    TechStackItem.objects.create(project=project, name=name, order=i)
                for img_data in images:
                    ProjectImage.objects.create(project=project, **img_data)
                self.stdout.write(self.style.SUCCESS(f"  Created: {project.name}"))
            else:
                self.stdout.write(f"  Skipped (exists): {project.name}")

        self.stdout.write(self.style.SUCCESS("Done."))
