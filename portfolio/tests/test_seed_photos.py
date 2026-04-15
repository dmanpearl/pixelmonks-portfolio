"""
Tests that seed_photos.PHOTOS and static/images/me/ are in sync.

- test_no_missing_images    : every PHOTOS entry has a real file on disk
- test_no_unreferenced_images: every file on disk is listed in PHOTOS
"""

from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase

from portfolio.management.commands.seed_photos import PHOTOS

ME_DIR = Path(settings.BASE_DIR) / "static" / "images" / "me"


class SeedPhotosConsistencyTest(SimpleTestCase):

    def setUp(self):
        self.disk_files = {f.name for f in ME_DIR.iterdir() if f.is_file() and not f.name.startswith(".")}
        self.seed_names = {Path(p["static_path"]).name for p in PHOTOS}

    def test_no_missing_images(self):
        """Every static_path in PHOTOS points to a file that exists on disk."""
        for photo in PHOTOS:
            path = Path(settings.BASE_DIR) / "static" / photo["static_path"]
            self.assertTrue(
                path.exists(),
                f"File referenced in seed_photos.PHOTOS is missing on disk: {photo['static_path']}",
            )

    def test_no_unreferenced_images(self):
        """Every file in static/images/me/ is referenced in PHOTOS."""
        unreferenced = self.disk_files - self.seed_names
        self.assertFalse(
            unreferenced,
            f"Files in static/images/me/ not referenced in seed_photos.PHOTOS: {sorted(unreferenced)}",
        )
