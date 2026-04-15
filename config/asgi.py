"""
ASGI config for pixelmonks-portfolio.

On Railway, set DJANGO_SETTINGS_MODULE=config.settings.prod in the Variables tab.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_asgi_application()
