from django.contrib import admin
from portfolio.models import Project, TechStackItem, ProjectImage, VisitorPreference


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


@admin.register(VisitorPreference)
class VisitorPreferenceAdmin(admin.ModelAdmin):
    list_display = ("visitor_key", "layout", "last_seen")
    readonly_fields = ("visitor_key", "last_seen")
