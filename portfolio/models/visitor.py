from django.db import models


class VisitorPreference(models.Model):
    """
    Stores lightweight display preferences keyed by IP + browser fingerprint.
    No personal data beyond IP is stored; used only for UX state persistence.
    """

    LAYOUT_CHOICES = [
        ("carousel", "Carousel"),
        ("grid", "Grid"),
        ("list", "List"),
    ]

    visitor_key = models.CharField(max_length=64, unique=True, db_index=True)
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICES, default="carousel")
    last_seen = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Visitor Preference"

    def __str__(self):
        return f"Visitor {self.visitor_key[:12]}… — {self.layout}"
