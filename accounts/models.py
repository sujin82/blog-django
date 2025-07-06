from django.contrib.auth.models import User
from django.db import models


def profile_img_path(instance, filename):
        ext = filename.split('.')[-1]
        return f'profiles/{instance.user.id}.{ext}'

class Profile(models.Model):
    # INTEREST_CHOICES = [
        
    # ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to=profile_img_path, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.BooleanField(blank=True, null=True)
    # interests = models.CharField() : 태그(10~20개) 제시하고 5개까지 다중선택 할 수 있게 제공할 예정
    def __str__(self):
        return f"{self.nickname.strip() or self.user.username}의 프로필"
    
    def get_gender_display(self):
        if self.gender is True:
            return "남성"
        elif self.gender is False:
            return "여성"
        else:
            return "미설정"
