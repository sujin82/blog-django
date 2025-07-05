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
    view_count = models.IntegerField(default=0)
    upload_img = models.ImageField(
        upload_to=user_post_upload_path, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.title
    
    