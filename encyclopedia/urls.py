from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("wiki/<str:title>/edit/", views.edit, name="edit"), 
    path("add", views.add, name="add"),
    path("search", views.search, name="search"),

]
