from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    slug = models.SlugField(unique=True, max_length=80)
    name = models.CharField(max_length=120)
    short_name = models.CharField(max_length=40, blank=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    description = models.TextField()
    involvement_percent = models.PositiveSmallIntegerField(default=100)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0, help_text="Lower numbers appear first")
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def hero_image(self):
        return self.images.filter(image_type="hero").first()

    @property
    def thumbnail_image(self):
        return self.images.filter(image_type="thumbnail").first() or self.images.first()

    @property
    def display_url(self):
        return self.url.replace("https://", "").replace("http://", "").rstrip("/")


class ProjectImageType:
    HERO = "hero"
    SCREENSHOT = "screenshot"
    THUMBNAIL = "thumbnail"
    MOBILE = "mobile"


class TechStackItem(models.Model):
    project = models.ForeignKey(Project, related_name="tech_stack", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.project} — {self.name}"
