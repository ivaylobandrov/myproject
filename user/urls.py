from django.urls import path

from user import views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("me/<str:pk>", views.me, name="me"),
]
