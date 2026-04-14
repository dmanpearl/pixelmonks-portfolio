import hashlib

from django.views.generic import ListView

from portfolio.models import Project, VisitorPreference


def _visitor_key(request):
    """SHA-256 of IP + User-Agent — no cookies, no auth."""
    raw = f"{request.META.get('REMOTE_ADDR', '')}{request.META.get('HTTP_USER_AGENT', '')}"
    return hashlib.sha256(raw.encode()).hexdigest()


class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.prefetch_related("tech_stack", "images").order_by("order", "name")

    def get(self, request, *args, **kwargs):
        # Persist layout preference if toggled via ?layout=grid|list
        layout = request.GET.get("layout")
        if layout in ("grid", "list"):
            key = _visitor_key(request)
            VisitorPreference.objects.update_or_create(
                visitor_key=key,
                defaults={"layout": layout},
            )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        key = _visitor_key(self.request)
        pref, _ = VisitorPreference.objects.get_or_create(visitor_key=key)
        ctx["layout"] = pref.layout
        ctx["featured_projects"] = Project.objects.filter(is_featured=True).prefetch_related(
            "tech_stack", "images"
        ).order_by("order")
        ctx["recent_projects"] = Project.objects.prefetch_related(
            "tech_stack", "images"
        ).order_by("-date_added")[:3]
        return ctx
