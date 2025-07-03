from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("blog/", views.post_list, name="post_list"),
    path("blog/<int:pk>/", views.post_detail, name="post_detail"),
    path("blog/write/", views.post_write, name="post_write"),
    path("blog/edit/<int:pk>/", views.post_edit, name="post_edit"),
    path("blog/delete/<int:pk>/", views.post_delete, name="post_delete"),
    path("blog/search/<str:tag>/", views.post_search, name="post_search"),
]