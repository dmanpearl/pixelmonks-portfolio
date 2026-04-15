# Pixelmonks Portfolio

Portfolio website for [pixelmonks.com](https://pixelmonks.com) — built with Python and Django.

## Local Development Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

cp .env.example .env
# Edit .env — set DJANGO_SECRET_KEY and RESEND_API_KEY (see Environment Variables below)

python manage.py migrate
python manage.py seed_projects
python manage.py createsuperuser
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000).
Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

`manage.py` defaults to `settings_dev` (SQLite, debug toolbar, `.env` loaded automatically).
Production uses `DJANGO_SETTINGS_MODULE=pixelmonks_portfolio.settings_prod`.

## Environment Variables

### Local (`.env`)

| Variable | Required | Description |
|---|---|---|
| `DJANGO_SECRET_KEY` | Yes | Django secret key — generate with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `RESEND_API_KEY` | Yes | From [resend.com](https://resend.com) — used by the contact form |

`DJANGO_DEBUG`, `DATABASE_URL`, and `DJANGO_ALLOWED_HOST` are **not** needed in `.env` — `settings_dev.py` handles them automatically.

### Railway (Production)

Set these in your Railway service's **Variables** panel:

| Variable | Value |
|---|---|
| `DJANGO_SETTINGS_MODULE` | `pixelmonks_portfolio.settings_prod` |
| `DJANGO_SECRET_KEY` | A strong random secret (never the dev key) |
| `RESEND_API_KEY` | Your Resend API key |
| `ALLOWED_HOSTS` | `pixelmonks.com,www.pixelmonks.com` |

Railway's **PostgreSQL plugin** auto-injects these — no manual entry needed:

| Variable | Injected by Railway |
|---|---|
| `PGDATABASE` | ✓ |
| `PGUSER` | ✓ |
| `PGPASSWORD` | ✓ |
| `PGHOST` | ✓ |
| `PGPORT` | ✓ |

## Code Formatting

```bash
black <file>.py               # Python
npx prettier --write <file>   # HTML / CSS
```

## Seeding Projects

```bash
python manage.py seed_projects          # insert (skips existing slugs)
python manage.py seed_projects --clear  # wipe all projects and re-insert
```

## Adding a New Portfolio Project

### 1. Add static images

Create a folder under `portfolio/static/portfolio/images/projects/<slug>/` and add your images:

```
portfolio/static/portfolio/images/projects/my-new-project/
├── screenshot.png   ← used as the hero / carousel image
└── logo.png         ← used as thumbnail
```

Commit these files — they deploy with the code and are served by WhiteNoise.

### 2. Add to the seed command

Add an entry to the `PROJECTS` list in `portfolio/management/commands/seed_projects.py`:

```python
{
    "slug": "my-new-project",
    "name": "MyApp.com",
    "url": "https://myapp.com",
    "github_url": "",          # leave blank if private
    "description": "2–3 sentences describing the project.",
    "involvement_percent": 100,
    "is_featured": True,       # True = appears in the hero carousel
    "order": 4,                # controls display order; lower = first
    "tech_stack": ["Python", "Django", "PostgreSQL"],
    "images": [
        {
            "static_path": "portfolio/images/projects/my-new-project/screenshot.png",
            "image_type": "hero",
            "caption": "",
            "order": 0,
        },
        {
            "static_path": "portfolio/images/projects/my-new-project/logo.png",
            "image_type": "thumbnail",
            "caption": "",
            "order": 1,
        },
    ],
},
```

Then run:

```bash
python manage.py seed_projects --clear
```

### 3. (Optional) Add via admin instead

Go to `/admin/` → **Projects** → **Add Project**. Fill in name, slug, URL, description, involvement, order, and check **Is featured** for the carousel. Add **Tech Stack Items** and **Project Images** inline.

For images added via admin: set the `Static path` field (e.g. `portfolio/images/projects/my-new-project/screenshot.png`) rather than uploading a file — uploaded files live in `media/` which is ephemeral on Railway.

---

## Project Structure

```
pixelmonks_portfolio/   Django project config (settings, urls, wsgi)
  settings.py           Base settings (shared)
  settings_dev.py       Dev overrides: SQLite, debug toolbar, dotenv
  settings_prod.py      Prod overrides: PostgreSQL, HTTPS security headers

portfolio/
  models/
    project.py          Project + TechStackItem
    project_image.py    ProjectImage — static_path (committed) or image (upload)
    visitor.py          VisitorPreference — grid/list layout by IP+browser hash
  views/
    project_list.py     Gallery + visitor layout preference
    project_detail.py   Single project
    contact.py          Contact form → Resend email
  templates/portfolio/
    project_list.html   Gallery (terminal hero + carousel + grid/list toggle)
    project_detail.html Project detail page
    contact.html        Contact form (name, email, phone, method, message)
    components/
      carousel.html     Featured projects carousel with thumb strip
      project_card.html Reusable card (adapts to grid and list layouts)
  static/portfolio/
    css/styles.css      All styles — Terminal Glass theme (violet + cyan + amber)
    js/main.js          Carousel JS (no framework)
    images/projects/    Committed project screenshots and logos
  management/commands/
    runserver.py        Suppresses the dev-server production warning
    seed_projects.py    Seed initial project data

templates/
  base.html             Global layout: nav, footer, Google Fonts
  icons_sprite.html     Inline SVG sprite — all icons defined here, referenced via <use>
  admin/login.html      Custom admin login with password visibility toggle
```

## Deployment to Railway

```bash
# First deploy or after model changes:
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py seed_projects   # safe to run; skips existing slugs
gunicorn pixelmonks_portfolio.wsgi
```

WhiteNoise serves all static files (including project images) — no CDN or Cloudinary required.
