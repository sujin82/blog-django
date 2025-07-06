from django.urls import path
from . import views
from accounts.views import ProfileUpdateView, login_view, logout_view
app_name = 'accounts'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/edit/", ProfileUpdateView.as_view(), name='profile_edit'),
]