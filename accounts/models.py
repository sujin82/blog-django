from django.contrib.auth.models import User
from django.db import models


def profile_img_path(instance, filename):
        ext = filename.split('.')[-1]
        return f'profiles/{instance.user.id}.{ext}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    upload_img = models.ImageField(upload_to=profile_img_path, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(blank=True, null=True) # 미사용
    gender = models.BooleanField(blank=True, null=True, default=None) # 미사용
    # interests = models.CharField() : 태그(10~20개) 제시하고 5개까지 다중선택 할 수 있게 제공할 예정
    def __str__(self):
        return f"{self.nickname.strip() or self.user.username}의 프로필"
    
    @property
    def profile_image_url(self):
        if self.upload_img:
            return self.upload_img.url
        else:
            return "/static/images/default-profile.png"
