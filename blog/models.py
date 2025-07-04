from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('travel', '여행'),
        ('food', '맛집'),
    ]
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='travel')
    # status = models.CharField(...) 상태관리(공개/비공개 설정)

    def __str__(self):
        return self.title
    
    