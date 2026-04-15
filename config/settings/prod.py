"""
config/settings/prod.py

Production settings. Selected on Railway via:

    DJANGO_SETTINGS_MODULE=config.settings.prod

Set this in the Railway dashboard under your service's Variables tab.
Never set DEBUG=True in this environment.
"""

from .base import *  # noqa: F401, F403

DEBUG = False

# WhiteNoise serves and compresses static files in production.
# Inserted right after SecurityMiddleware (position 1).
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "portfolio.middleware.WwwRedirectMiddleware",
] + MIDDLEWARE[1:]  # noqa: F405

# Content-hash filenames enable far-future cache headers. Only safe when DEBUG=False.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# HTTPS hardening
# Tell Django to trust Railway's reverse proxy — it terminates SSL and forwards
# requests as plain HTTP with X-Forwarded-Proto: https. Without this,
# SECURE_SSL_REDIRECT causes an infinite redirect loop.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
