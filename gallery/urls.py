from django.urls import path

from . import views


urlpatterns = [
    path("gallery/create-card", views.create_presentation_card, name="create-card"),
    path("", views.PresentationCardsView.as_view(), name="gallery"),
    path("gallery/<str:pk>/delete/", views.delete_presentation_card, name="delete-presentation-card"),
    path("gallery/<str:pk>/update/", views.update_presentation_card, name="update-presentation-card"),
    path("gallery/<str:pk>/presentation-card/", views.ShowPresentationCardInfoView.as_view(), name="presentation-card"),
]
