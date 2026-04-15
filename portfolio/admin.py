from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from portfolio.models import Project, TechStackItem, ProjectImage, SiteSettings, VisitorPreference


class TechStackInline(admin.TabularInline):
    model = TechStackItem
    extra = 1
    fields = ("name", "order")


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "image_type", "caption", "order")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "involvement_percent", "is_featured", "order", "date_added")
    list_editable = ("is_featured", "order")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [TechStackInline, ProjectImageInline]


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fields = ("contact_enable",)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Skip the list — go straight to the one record (create it if missing)
        obj = SiteSettings.get()
        return HttpResponseRedirect(
            reverse("admin:portfolio_sitesettings_change", args=[obj.pk])
        )


@admin.register(VisitorPreference)
class VisitorPreferenceAdmin(admin.ModelAdmin):
    list_display = ("visitor_key", "layout", "last_seen")
    readonly_fields = ("visitor_key", "last_seen")
