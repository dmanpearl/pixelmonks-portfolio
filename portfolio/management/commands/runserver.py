import os
import sys
from datetime import datetime

from django.conf import settings
from django.utils.version import get_docs_version
from django.core.management.commands.runserver import Command as BaseCommand


class Command(BaseCommand):
    """Runserver without the production-warning noise in dev."""

    def on_bind(self, server_port):
        quit_command = "CTRL-BREAK" if sys.platform == "win32" else "CONTROL-C"

        if self._raw_ipv6:
            addr = f"[{self.addr}]"
        elif self.addr == "0":
            addr = "0.0.0.0"
        else:
            addr = self.addr

        now = datetime.now().strftime("%B %d, %Y - %X")
        version = self.get_version()
        print(
            f"{now}\n"
            f"Django version {version}, using settings {settings.SETTINGS_MODULE!r}\n"
            f"Starting development server at {self.protocol}://{addr}:{server_port}/\n"
            f"Quit the server with {quit_command}.",
            file=self.stdout,
        )
        # Warning intentionally omitted in development.
