import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


def user_post_upload_path(instance, filename):
    username = instance.author.username
    date_str = datetime.now().strftime('%Y%m%d')

    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex}.{ext}'

    return f'posts/{username}/{date_str}/{new_filename}'

# 게시글
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    CATEGORY_CHOICES = [
        ('travel', '여행'),
        ('food', '맛집'),
    ]
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='travel'
    )
    # status = models.CharField(...) 상태관리(공개/비공개 설정)
    upload_img = models.ImageField(
        upload_to=user_post_upload_path, 
        blank=True, 
        null=True
    )

    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at'] 
    
    


# 좋아요
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'post')




# 댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)