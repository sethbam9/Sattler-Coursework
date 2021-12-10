from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="entry"),
    path("results/", views.search_results, name="results"),
    path("create/", views.create_entry, name="create"),
    path("create/save", views.save_entry, name="save"),
    path("wiki/<str:title>/edit", views.edit_entry, name="edit"),
    path("random/", views.random_entry, name="random"),
]
