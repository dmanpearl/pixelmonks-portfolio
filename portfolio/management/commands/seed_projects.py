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
        "short_name": "Ratings",
        "url": "https://ratingranch.com",
        "github_url": "",
        "description": (
            "Sports ratings platform featuring data import via Excel spreadsheets, "
            "Pandas-powered analytics, and public leaderboards. Built for the Alliance "
            "Sports organization to manage and publish competitive ratings across multiple "
            "basketball, hockey, and baseball divisions."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 2,
        "tech_stack": [
            "Python",
            "Django",
            "PostgreSQL",
            "Pandas",
            "OpenPyXL",
            "FastAPI",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/rating-ranch/screenshot.png",
                "image_type": "hero",
                "caption": "The team schedule displays game stats and color-codes win/loss outcomes",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-home.png",
                "image_type": "gallery",
                "caption": "Home dashboard showing division standings and recent activity",
                "order": 2,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-home2.png",
                "image_type": "gallery",
                "caption": "Alternate home view with featured matchups and top-rated players",
                "order": 3,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-matchup-nba.png",
                "image_type": "gallery",
                "caption": "NBA head-to-head matchup ratings with predictive scoring",
                "order": 4,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-schedule-nba.png",
                "image_type": "gallery",
                "caption": "NBA schedule view with game outcomes and rating impact",
                "order": 5,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-schedule-lakers.png",
                "image_type": "gallery",
                "caption": "Lakers season schedule with win/loss record and rating trends",
                "order": 6,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-players-nba.png",
                "image_type": "gallery",
                "caption": "NBA player leaderboard with sortable ratings and stats",
                "order": 7,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-players-cbb.png",
                "image_type": "gallery",
                "caption": "College basketball player rankings across all tracked divisions",
                "order": 8,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-roster-nba-warriors.png",
                "image_type": "gallery",
                "caption": "Golden State Warriors full roster with individual player ratings",
                "order": 9,
            },
            {
                "static_path": "portfolio/images/projects/rating-ranch/gallery-player-detail.png",
                "image_type": "gallery",
                "caption": "Player detail page showing rating history and game-by-game breakdown",
                "order": 10,
            },
        ],
    },
    {
        "slug": "breaking-news-guys",
        "name": "BreakingNewsGuys.com",
        "short_name": "News",
        "url": "https://breakingnewsguys.com",
        "github_url": "",
        "description": (
            "Breaking News broadcasting platform for a stock-based news team. "
            "Editors compose messages and dispatch them simultaneously to multiple clients "
            "including ASGI streaming endpoints, Discord webhooks, and Slack messages. "
            "Supports binary attachments, media uploads, API documentation via FastAPI "
            "and Swagger, and example clients."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 3,
        "tech_stack": [
            "Python",
            "Django",
            "PostgreSQL",
            "ASGI",
            "Cloudinary",
            "FastAPI",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/breaking-news/screenshot.png",
                "image_type": "hero",
                "caption": "Multimedia messages are composed and broadcast in real time to all configured destinations",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/breaking-news/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
            {
                "static_path": "portfolio/images/projects/breaking-news/gallery-new.png",
                "image_type": "gallery",
                "caption": "Message composer with rich text, media attachments, and multi-destination targeting",
                "order": 2,
            },
            {
                "static_path": "portfolio/images/projects/breaking-news/gallery-message.png",
                "image_type": "gallery",
                "caption": "Published message detail with attachment preview and delivery status",
                "order": 3,
            },
            {
                "static_path": "portfolio/images/projects/breaking-news/gallery-reader.png",
                "image_type": "gallery",
                "caption": "Subscriber reader view with real-time streaming updates",
                "order": 4,
            },
            {
                "static_path": "portfolio/images/projects/breaking-news/gallery-api.png",
                "image_type": "gallery",
                "caption": "FastAPI and Swagger auto-generated API documentation",
                "order": 5,
            },
            {
                "static_path": "portfolio/images/projects/breaking-news/gallery-api-usage.png",
                "image_type": "gallery",
                "caption": "API usage log with per-client message history and delivery tracking",
                "order": 6,
            },
        ],
    },
    {
        "slug": "la-surfing-school",
        "name": "LAsurfing.school",
        "short_name": "Surfing",
        "url": "https://lasurfing.school",
        "github_url": "",
        "description": (
            "Marketing and lesson-booking website for a Los Angeles surf instructor. "
            "Integrates Stripe for payment processing and Resend for transactional "
            "booking confirmation emails, with a student review and 5-star rating system."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 4,
        "tech_stack": [
            "Python",
            "Django",
            "PostgreSQL",
            "Stripe",
            "Resend",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/la-surfing-school/screenshot.png",
                "image_type": "hero",
                "caption": "Full-featured surf school site with lesson booking, Stripe payments, and student ratings",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/la-surfing-school/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
            {
                "static_path": "portfolio/images/projects/la-surfing-school/gallery-lessons.png",
                "image_type": "gallery",
                "caption": "Lesson catalog with duration, skill level, and pricing options",
                "order": 2,
            },
            {
                "static_path": "portfolio/images/projects/la-surfing-school/gallery-booking.png",
                "image_type": "gallery",
                "caption": "Stripe-powered booking flow with date selection and instant confirmation",
                "order": 3,
            },
            {
                "static_path": "portfolio/images/projects/la-surfing-school/gallery-ratings.png",
                "image_type": "gallery",
                "caption": "5-star rating system with verified student reviews",
                "order": 4,
            },
            {
                "static_path": "portfolio/images/projects/la-surfing-school/gallery-contact.png",
                "image_type": "gallery",
                "caption": "Contact form with Resend transactional email confirmation",
                "order": 5,
            },
        ],
    },
    {
        "slug": "gnarbox",
        "name": "Gnarbox",
        "short_name": "Gnarbox",
        "url": "https://photographylife.com/reviews/gnarbox-2-0-ssd",
        "url_label": "Photographylife",
        "github_url": "",
        "description": (
            "At Gnarbox, I was part of the original engineering team building a rugged, "
            "portable media device for photographers and videographers working in the field. "
            "I contributed across the stack, from embedded microservices on the device to "
            "mobile app controllers, delivering high-throughput RAW and 4K media ingestion, "
            "processing, and backup without a laptop. My work included Go services, gRPC and "
            "Protobuf APIs, containerized components, CI/CD pipelines and DevOps practices, "
            "and mobile development in React Native, Swift, and Android Java, along with "
            "media pipelines using GStreamer. As the team grew to eight developers within "
            "a 20-person company, we shipped a globally recognized product known for "
            "performance, reliability, and innovation in extreme environments."
        ),
        "involvement_percent": 8,
        "is_featured": True,
        "order": 5,
        "tech_stack": [
            "Go",
            "React Native",
            "Docker",
            "DevOps",
            "CI/CD",
            "Swift",
            "Android Java",
            "gRPC/Protobuf",
            "GStreamer",
            "Node.js/TypeScript",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/gnarbox/screenshot.jpg",
                "image_type": "hero",
                "caption": "Gnarbox was controlled via the onboard OSD or the Gnarbox Mobile App",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/gnarbox/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
            {
                "static_path": "portfolio/images/projects/gnarbox/gnarbox_package_plus_app.png",
                "image_type": "gallery",
                "caption": "Retail package included the Gnarbox device and accessories",
                "order": 2,
            },
            {
                "static_path": "portfolio/images/projects/gnarbox/gnarbox_video_clip.jpg",
                "image_type": "gallery",
                "caption": "Video editing includes trimming, clipping, and merging of 4K footage and more",
                "order": 3,
            },
            {
                "static_path": "portfolio/images/projects/gnarbox/gnarbox_video_edit.jpeg",
                "image_type": "gallery",
                "caption": "Audio sync tools for aligning video with external audio sources",
                "order": 4,
            },
            {
                "static_path": "portfolio/images/projects/gnarbox/gnarbox_settings.jpg",
                "image_type": "gallery",
                "caption": "Multi-destination backup with verification, smart copy options, and configurable safety rules",
                "order": 5,
            },
            {
                "static_path": "portfolio/images/projects/gnarbox/gnarbox_image_gallery.jpg",
                "image_type": "gallery",
                "caption": "Native media browser handles tens of thousands of thumbnails with smooth scrolling",
                "order": 6,
            },
        ],
    },
    {
        "slug": "leaderlodge",
        "name": "LeaderLodge",
        "short_name": "AI Insights",
        "url": "https://leaderlodge.com",
        "github_url": "",
        "description": (
            "Computed by LeaderLodge. Explained by AI. Web app for "
            "groups who play games together: record scores, track rankings and "
            "leaderboards, and interrogate your stats with natural-language questions. "
            "Two AI modes power the experience: contextual Insights that narrate "
            "standings and trends, and an agentic Ask feature that uses tool-calling "
            "across live stats to answer freeform questions. "
            "Supports Dominoes, Backgammon, Mah Jongg, Progressive "
            "Rummy, and more, with group rosters, matchups, Hall of Fame history, "
            "and a public demo mode."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 1,
        "tech_stack": [
            "Python",
            "Django",
            "PostgreSQL",
            "OpenAI",
            "Google Gemini",
            "Railway",
            "Brevo",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/leaderlodge/screenshot.png",
                "image_type": "hero",
                "caption": (
                    "Home dashboard with leaderboards, recent games, and AI game insights"
                ),
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-leaderboard.png",
                "image_type": "gallery",
                "caption": (
                    "Leaderboard ranks players by weighted finish points, with an "
                    "Insights panel for AI summaries of standings and trends"
                ),
                "order": 2,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-games.png",
                "image_type": "gallery",
                "caption": "Game history list with filterable columns for player, location, and date",
                "order": 3,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-game.png",
                "image_type": "gallery",
                "caption": (
                    "Game detail with scores, placements, and contextual AI insights "
                    "from computed stats"
                ),
                "order": 4,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-add.png",
                "image_type": "gallery",
                "caption": "Record a new game with fuzzy player search and instant score preview",
                "order": 5,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-stats.png",
                "image_type": "gallery",
                "caption": (
                    "Head-to-head matchup stats with AI-generated narrative from "
                    "LeaderLodge-computed rankings"
                ),
                "order": 6,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-rummy.png",
                "image_type": "gallery",
                "caption": "Progressive Rummy scoring with round-by-round cumulative totals",
                "order": 7,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-halloffame.png",
                "image_type": "gallery",
                "caption": (
                    "Hall of Fame highlights period leaders with AI trend analysis "
                    "from computed history"
                ),
                "order": 8,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-dashboard.png",
                "image_type": "gallery",
                "caption": "Dashboard overview with leaderboard cards for each active game type",
                "order": 9,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-groups.png",
                "image_type": "gallery",
                "caption": "Groups view for managing players, roles, and game history per group",
                "order": 10,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-about.png",
                "image_type": "gallery",
                "caption": "About page describing the app's purpose and supported game types",
                "order": 11,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-about-ai-insights.png",
                "image_type": "gallery",
                "caption": "About page highlighting the AI-powered insights and analysis features",
                "order": 12,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-ai1.png",
                "image_type": "gallery",
                "caption": "AI-generated game commentary and statistical trend analysis",
                "order": 13,
            },
            {
                "static_path": "portfolio/images/projects/leaderlodge/gallery-ai-hall-of-fame.png",
                "image_type": "gallery",
                "caption": "AI-written Hall of Fame narrative celebrating top performers",
                "order": 14,
            },
        ],
    },
    {
        "slug": "leroys",
        "name": "Leroys Sports Betting App",
        "short_name": "Leroys",
        "url": "",
        "github_url": "",
        "description": (
            "One for the history books: in an era when location services were not "
            "available for browsers and smartphone location could easily be spoofed, "
            "Leroy's Sports Betting App was a groundbreaking mobile platform in 2010 and "
            "the first app of any kind approved by the Nevada Gaming Control Board for "
            "legal sports wagering. It was initially launched on BlackBerry and later "
            "expanded to Android and iOS. As the sole developer, I built the app "
            "for Leroy's, a subsidiary of American Wagering, helping pioneer U.S. "
            "mobile betting, attract William Hill's acquisition, and implement the "
            "rebranding to William Hill's mobile sportsbook across smartphone platforms."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 7,
        "tech_stack": [
            "Objective-C",
            "Android Java",
            "J2ME",
            "GPS Location Services",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/leroys/screenshot.png",
                "image_type": "hero",
                "caption": "This relic was once the most secure device on the market",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/leroys/logo.jpeg",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
        ],
    },
    {
        "slug": "manpearl-website",
        "name": "Personal Website",
        "short_name": "Manpearl",
        "url": "https://manpearl.com",
        "github_url": "https://github.com/dmanpearl/manpearl-website",
        "description": (
            "Minimal personal website serving as a professional hub with links "
            "to portfolio, LinkedIn, and GitHub."
        ),
        "involvement_percent": 100,
        "is_featured": True,
        "order": 6,
        "tech_stack": [
            "HTML",
            "CSS",
        ],
        "images": [
            {
                "static_path": "portfolio/images/projects/manpearl-website/screenshot.png",
                "image_type": "hero",
                "caption": "Personal website with links to portfolio, LinkedIn, and GitHub",
                "order": 0,
            },
            {
                "static_path": "portfolio/images/projects/manpearl-website/logo.png",
                "image_type": "thumbnail",
                "caption": "",
                "order": 1,
            },
            {
                "static_path": "portfolio/images/projects/manpearl-website/gallery-landing.png",
                "image_type": "gallery",
                "caption": (
                    "Provides access to Pixelmonks portfolio, LinkedIn, and GitHub"
                ),
                "order": 2,
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the database with initial portfolio projects"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear", action="store_true", help="Delete all projects before seeding"
        )
        parser.add_argument(
            "--override",
            action="store_true",
            help="Update existing projects from seed data",
        )

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
            elif options["override"]:
                for field, value in data.items():
                    if field != "slug":
                        setattr(project, field, value)
                project.save()
                project.tech_stack.all().delete()
                for i, name in enumerate(tech):
                    TechStackItem.objects.create(project=project, name=name, order=i)
                project.images.all().delete()
                for img_data in images:
                    ProjectImage.objects.create(project=project, **img_data)
                self.stdout.write(self.style.SUCCESS(f"  Updated: {project.name}"))
            else:
                self.stdout.write(f"  Skipped (exists): {project.name}")

        self.stdout.write(self.style.SUCCESS("Done."))
