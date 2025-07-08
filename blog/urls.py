from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("my-posts/", views.MyPostListView.as_view(), name="my_posts"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("write/", views.PostCreateView.as_view(), name="post_write"),
    path("edit/<int:pk>/", views.PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
    path("search/", views.PostSearchView.as_view(), name="post_search"),
    path("my-posts/search/", views.MyPostSearchView.as_view(), name="my_post_search"),
    path("<int:pk>/like/", views.ToggleLikeView.as_view(), name="toggle_like"),
    path("<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment_new"),
    path("<int:pk>/comments/edit/", views.comment_update_ajax, name="comment_update_ajax"),
    path("<int:pk>/comments/delete/", views.comment_delete_ajax, name="comment_delete_ajax"),
]
