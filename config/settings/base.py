"""
config/settings/base.py

Shared settings for all environments. Never use this file directly.
Import it in dev.py or prod.py.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env if present (local dev). In production, Railway injects env vars
# directly — load_dotenv is a harmless no-op there. override=True ensures
# local .env values win over any vars injected by `railway run`.
load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env", override=True)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")
if not SECRET_KEY:
    raise RuntimeError(
        "DJANGO_SECRET_KEY is not set. "
        "Copy .env.example to .env and fill in a secret key."
    )

# Allowed hosts — canonical domain + Railway subdomain for health checks.
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "pixelmonks.com",
    "pixelmonks-portfolio.up.railway.app",
]
_custom = os.environ.get("DJANGO_ALLOWED_HOST", "")
if _custom:
    ALLOWED_HOSTS.append(_custom)

# Required for Railway's HTTPS proxy and for CSRF to work in production.
CSRF_TRUSTED_ORIGINS = [
    "https://pixelmonks.com",
    "https://pixelmonks-portfolio.up.railway.app",
]
if _custom:
    CSRF_TRUSTED_ORIGINS.append(f"https://{_custom}")

# Keep CSRF cookie alive 1 year; session expires after 2 weeks of inactivity.
CSRF_COOKIE_AGE = 60 * 60 * 24 * 365   # 1 year
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14  # 2 weeks
SESSION_SAVE_EVERY_REQUEST = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolio",
]

# WhiteNoise is added in prod.py only. In dev, Django's built-in static
# file serving is used so staticfiles are always fresh without collectstatic.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "portfolio.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ── Database ──────────────────────────────────────────────────────────────────
# Railway injects DATABASE_URL automatically when a Postgres plugin is added.
# Locally: no DATABASE_URL → falls back to SQLite.
_db_url = os.environ.get("DATABASE_URL", "")
if _db_url:
    import urllib.parse as _up

    _u = _up.urlparse(_db_url)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": _u.path.lstrip("/"),
            "USER": _u.username,
            "PASSWORD": _u.password,
            "HOST": _u.hostname,
            "PORT": str(_u.port or 5432),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
            "OPTIONS": {"timeout": 30},
        }
    }

# ── Auth ──────────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ── Internationalisation ──────────────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Los_Angeles"
USE_I18N = True
USE_TZ = True

# ── Static / Media ────────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ── Resend (contact form) ─────────────────────────────────────────────────────
# RESEND_API_KEY is optional here; contact form is gated by SiteSettings.
RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
CONTACT_FROM_EMAIL = "Pixelmonks Contact <info@pixelmonks.com>"
CONTACT_TO_EMAIL = "dmanpearl@pixelmonks.com"

# ── Logging ───────────────────────────────────────────────────────────────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "iso_timestamp": {
            "format": "{asctime} {levelname} {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "iso_timestamp",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
