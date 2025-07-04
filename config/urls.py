from django.contrib import admin
from django.urls import path, include
from accounts.views import login, logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
