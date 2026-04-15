"""
Seed Photo records for the about page carousel.

Usage:
    python manage.py seed_photos          # insert / update auto_caption only
    python manage.py seed_photos --clear  # wipe and re-insert everything

Rules:
  - auto_caption is always updated to the value in this file.
  - caption (the editable one) is only set from auto_caption if it is currently
    blank — so your Admin edits are never overwritten on re-run.
  - --clear resets both fields (use only when you want a clean slate).
"""

from django.core.management.base import BaseCommand
from portfolio.models import Photo


PHOTOS = [
    {
        "static_path": "images/me/1985_David_Hughes_Aircraft_Company_El_Segundo_CA.jpg",
        "auto_caption": "Early Programmable Test Station, Hughes Aircraft Company, El Segundo CA",
        "order": 2,
    },
    {
        "static_path": "images/me/2005_David_wins_San_Clemente_Circuit_Race_Cat_4_CA.jpg",
        "auto_caption": "San Clemente Circuit Race, Cat 4 winner",
        "order": 18,
    },
    {
        "static_path": "images/me/2018-03-14_Gnarbox_office_Santa_Monica_CA.jpg",
        "auto_caption": "Gnarbox Office, Santa Monica CA",
        "order": 3,
    },
    {
        "static_path": "images/me/2018-06-05_Yosemite_National_Park_CA.jpg",
        "auto_caption": "Yosemite National Park CA",
        "order": 4,
    },
    {
        "static_path": "images/me/2019-05-19_Gnarbox_location_unknown.JPG",
        "auto_caption": "Building the Gnarbox in the field",
        "order": 5,
    },
    {
        "static_path": "images/me/2019-18-16_Yosemite_Valley_Half_Dome_Merced_River_CA.jpg",
        "auto_caption": "Yosemite Valley — Half Dome & Merced River CA",
        "order": 6,
    },
    {
        "static_path": "images/me/2020-05-29_David_at_home_Venice_CA.jpeg",
        "auto_caption": "At Home, Venice CA",
        "order": 7,
    },
    {
        "static_path": "images/me/2021-05-02_David_Switzer_Trail_Altadena_CA.jpeg",
        "auto_caption": "Switzer Trail, Altadena CA",
        "order": 8,
    },
    {
        "static_path": "images/me/2021-10-29_David_Four_Corners_Moab_UT.jpeg",
        "auto_caption": "Four Corners, Moab UT",
        "order": 9,
    },
    {
        "static_path": "images/me/2022-01-05_David_Santa_Catalina_Island_CA.jpg",
        "auto_caption": "Santa Catalina Island CA",
        "order": 10,
    },
    {
        "static_path": "images/me/2022-07-23_David_OWC_Company_Picnic_2022_Volleyball_Woodstock_IL.jpg",
        "auto_caption": "OWC Company Picnic 2022 Volleyball, Woodstock IL",
        "order": 11,
    },
    {
        "static_path": "images/me/2023-05-13_David_Office_Venice_CA.jpg",
        "auto_caption": "Office, Venice CA",
        "order": 12,
    },
    {
        "static_path": "images/me/2023-11-12_David_White_Sands_National_Park_NM.jpg",
        "auto_caption": "White Sands National Park NM",
        "order": 13,
    },
    {
        "static_path": "images/me/2023-11-23_David_Sequoia_National_Park_CA.jpg",
        "auto_caption": "Sequoia National Park CA",
        "order": 14,
    },
    {
        "static_path": "images/me/2023-11-30_David_St_David_AZ.jpeg",
        "auto_caption": "St. David AZ",
        "order": 15,
    },
    {
        "static_path": "images/me/2024-10-26_David_Grayland_Beach_State_Park_WA.jpeg",
        "auto_caption": "Grayland Beach State Park WA",
        "order": 16,
    },
    {
        "static_path": "images/me/2024-10-28_David_Lake_Quinault_WA_.jpg",
        "auto_caption": "Lake Quinault WA",
        "order": 17,
    },
]


class Command(BaseCommand):
    help = "Seed Photo records for the about page carousel"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear", action="store_true", help="Delete all photos before seeding"
        )

    def handle(self, *args, **options):
        if options["clear"]:
            Photo.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared all photos."))

        for data in PHOTOS:
            photo, created = Photo.objects.get_or_create(
                static_path=data["static_path"],
                defaults={
                    "auto_caption": data["auto_caption"],
                    "caption": data[
                        "auto_caption"
                    ],  # seed caption on first create only
                    "order": data["order"],
                },
            )
            if not created:
                # Always refresh auto_caption and order; never touch caption
                photo.auto_caption = data["auto_caption"]
                photo.order = data["order"]
                photo.save(update_fields=["auto_caption", "order"])
                self.stdout.write(f"  Updated (kept caption): {photo.auto_caption}")
            else:
                self.stdout.write(
                    self.style.SUCCESS(f"  Created: {photo.auto_caption}")
                )

        self.stdout.write(self.style.SUCCESS("Done."))
