import random

from django.views.generic import TemplateView

from portfolio.models import Photo


class AboutView(TemplateView):
    template_name = "portfolio/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(Photo.objects.all())
        random.shuffle(photos)
        context["photos"] = photos
        return context
