from django.db import models


class Photo(models.Model):
    static_path = models.CharField(max_length=200)
    auto_caption = models.CharField(
        max_length=200,
        help_text="Auto-generated from filename. Never edited directly.",
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Displayed caption. Edit this freely — seed command will not overwrite it.",
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.caption or self.auto_caption

    @property
    def display_caption(self):
        return self.caption or self.auto_caption
