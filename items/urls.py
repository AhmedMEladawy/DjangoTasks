from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("tracks/", views.tracks, name="tracks"),
    path("tracks/<int:id>/", views.tracks_show, name="tracks_show"),
    path("tracks/<int:id>/delete/", views.tracks_delete, name="tracks_delete"),   
    path("tracks/<int:id>/update/", views.tracks_update, name="tracks_update"), 
    path("contact/", views.contact, name="contact"),
    path("category.html/", views.category, name="category"),
]
