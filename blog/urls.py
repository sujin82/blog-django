from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("write/", views.PostCreateView.as_view(), name="post_write"),
    path("edit/<int:pk>/", views.PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
    # path("blog/search/<str:tag>/", views.post_search, name="post_search"),
    path('<int:pk>/like/', views.ToggleLikeView.as_view(), name='toggle_like'),
    path('<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new')
]