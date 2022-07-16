from django.urls import path

from gallery import views

urlpatterns = [
    path("create-card/", views.create_presentation_card, name="create-card"),
    path("", views.show_cards, name="gallery"),
    path("presentation-cards/api/", views.show_cards_info, name="cards_api"),
    path("presentation-card/<str:pk>/", views.show_card, name="presentation-card"),
    path("presentation-card/<str:pk>/api/", views.show_card_info, name="card_api"),
    path("presentation-card/<str:pk>/delete/", views.delete_presentation_card, name="delete-presentation-card"),
    path("presentation-card/<str:pk>/update/", views.update_presentation_card, name="update-presentation-card"),
]
