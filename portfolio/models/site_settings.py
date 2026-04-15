from django.db import models


class SiteSettings(models.Model):
    contact_enable = models.BooleanField(
        default=False,
        help_text="Show the Contact link and enable the /contact/ page.",
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        # Enforce singleton: always write to pk=1
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Singleton — never delete via ORM
        pass

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
