from django.urls import path

from . import views


urlpatterns = [
    path("gallery/create-card", views.create_presentation_card, name="create-card"),
    path("", views.show_cards, name="gallery"),
    path("gallery/cards/api", views.show_cards_info, name="cards_api"),
    path("gallery/<str:pk>/presentation-card/", views.show_card, name="presentation-card"),
    path("gallery/card/<str:pk>/api", views.show_card_info, name="card_api"),
    path("gallery/<str:pk>/delete/", views.delete_presentation_card, name="delete-presentation-card"),
    path("gallery/<str:pk>/update/", views.update_presentation_card, name="update-presentation-card"),
]
