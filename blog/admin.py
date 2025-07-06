from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_filter = ["category"]
    search_fields = ["title"] 


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'created_at']  # 필드명은 실제 모델에 맞게 수정
    list_filter = ['created_at']
    search_fields = ['content']
