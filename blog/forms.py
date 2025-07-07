from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'upload_img', 'ai_auto_reply']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']