"""
config/settings/dev.py

Development settings. Selected automatically by manage.py.
Never use this file on Railway or any production server.

Requires: pip install -r requirements-dev.txt  (adds django-debug-toolbar)
"""

from .base import *  # noqa: F401, F403

DEBUG = True

# Django Debug Toolbar — installed via requirements-dev.txt only.
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405

INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_COLLAPSED": True,
}
