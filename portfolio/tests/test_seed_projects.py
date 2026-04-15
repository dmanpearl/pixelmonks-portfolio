"""
Tests that seed_projects.PROJECTS and portfolio/static/portfolio/images/projects/
are in sync.

- test_no_missing_images        : every image entry has a real file on disk
- test_no_unreferenced_images   : every file in the projects image dir is referenced
"""

from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase

from portfolio.management.commands.seed_projects import PROJECTS

PROJECTS_IMG_DIR = (
    Path(settings.BASE_DIR) / "portfolio" / "static" / "portfolio" / "images" / "projects"
)


class SeedProjectsConsistencyTest(SimpleTestCase):

    def setUp(self):
        # Collect all files on disk under images/projects/
        self.disk_files = {
            f.relative_to(Path(settings.BASE_DIR) / "portfolio" / "static").as_posix()
            for f in PROJECTS_IMG_DIR.rglob("*")
            if f.is_file() and not f.name.startswith(".")
        }
        # Collect all static_paths referenced in PROJECTS
        self.seed_paths = {
            img["static_path"]
            for project in PROJECTS
            for img in project["images"]
        }

    def test_no_missing_images(self):
        """Every image static_path in PROJECTS exists on disk."""
        for project in PROJECTS:
            for img in project["images"]:
                path = Path(settings.BASE_DIR) / "portfolio" / "static" / img["static_path"]
                self.assertTrue(
                    path.exists(),
                    f"File referenced in PROJECTS['{project['slug']}'] is missing on disk: {img['static_path']}",
                )

    def test_no_unreferenced_images(self):
        """Every file under portfolio/static/portfolio/images/projects/ is referenced in PROJECTS."""
        unreferenced = self.disk_files - self.seed_paths
        self.assertFalse(
            unreferenced,
            f"Image files not referenced in seed_projects.PROJECTS: {sorted(unreferenced)}",
        )
