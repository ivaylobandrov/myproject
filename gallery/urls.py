from django.urls import path

from . import views


urlpatterns = [
    path("gallery/create-card", views.create_presentation_card, name="create-card"),
    path("", views.show_card, name="gallery"),
    path("gallery/<str:pk>/delete/", views.delete_presentation_card, name="delete-presentation-card"),
    path("gallery/<str:pk>/update/", views.update_presentation_card, name="update-presentation-card"),
    path("gallery/cards/api", views.show_presentation_cards_info, name="test"),
    path("gallery/<str:pk>/presentation-card/", views.show_card, name="presentation-card"),
]
