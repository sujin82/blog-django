from django.urls import path
from . import views
from accounts.views import login_view, logout_view

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]