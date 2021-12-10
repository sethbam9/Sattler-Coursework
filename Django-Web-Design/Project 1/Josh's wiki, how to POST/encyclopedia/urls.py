from django.urls import path

from . import views

# All url pattern that are used in the encyclopedia app.
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("error/<str:message>", views.error, name="error"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("edit", views.edit, name="edit"),
    path("random", views.random_entry, name="random")
]
