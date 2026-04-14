from django.urls import path
from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project_list"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="project_detail"),
]
