from django.db import models
from django.templatetags.static import static


class ProjectImage(models.Model):
    class ImageType(models.TextChoices):
        HERO = "hero", "Hero"
        SCREENSHOT = "screenshot", "Screenshot"
        THUMBNAIL = "thumbnail", "Thumbnail"
        MOBILE = "mobile", "Mobile"

    project = models.ForeignKey(
        "portfolio.Project", related_name="images", on_delete=models.CASCADE
    )
    # For admin-uploaded images (future: Cloudinary in production)
    image = models.ImageField(upload_to="projects/", blank=True)
    # For developer-committed images served via WhiteNoise
    # e.g. "portfolio/images/projects/rating-ranch/screenshot.png"
    static_path = models.CharField(max_length=200, blank=True)
    image_type = models.CharField(max_length=20, choices=ImageType.choices, default=ImageType.SCREENSHOT)
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.project} — {self.image_type}"

    @property
    def url(self):
        """Returns the URL for whichever image source is set."""
        if self.static_path:
            return static(self.static_path)
        if self.image:
            return self.image.url
        return ""
