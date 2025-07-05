from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login, logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]

if settings.DEBUG:  # 개발 환경에서만 사용
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)