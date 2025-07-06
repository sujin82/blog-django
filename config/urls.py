from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main_page, name="main"),
    path("blog/", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:  # 개발 환경에서만 사용
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)