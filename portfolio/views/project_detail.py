from django.views.generic import DetailView

from portfolio.models import Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Project.objects.prefetch_related("tech_stack", "images")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = list(Project.objects.order_by("order", "id").only("id", "slug", "name"))
        try:
            idx = next(i for i, p in enumerate(projects) if p.id == self.object.id)
        except StopIteration:
            idx = -1
        context["first_project"] = projects[0] if idx > 0 else None
        context["prev_project"] = projects[idx - 1] if idx > 0 else None
        context["next_project"] = projects[idx + 1] if idx < len(projects) - 1 else None
        context["last_project"] = projects[-1] if idx < len(projects) - 1 else None
        images = list(self.object.images.all())
        context["screenshot_images"] = [img for img in images if img.image_type in ("screenshot", "mobile")]
        context["gallery_images"] = [img for img in images if img.image_type == "gallery"]
        return context
