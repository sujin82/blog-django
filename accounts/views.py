from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegisterForm, ProfileForm
from accounts.models import Profile


def register(request):  # CBV로 변경 예정
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

            # 자동 로그인 처리
            raw_password = user_form.cleaned_data["password1"] # 해싱
            username = user_form.cleaned_data["username"]
            user = authenticate(request, username=username, password=raw_password)

            if user:
                login(request, user)
                messages.success(request, "회원가입이 완료되었습니다.")
                return redirect("/")
            else:
                messages.error(request, "자동 로그인에 실패했습니다. 로그인 페이지로 이동합니다.")
                return redirect("/login/")
        else:
            messages.error(request, "입력 정보를 다시 확인해주세요.")
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()

    return render(request, "accounts/register_form.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })



# 로그인/로그아웃
login_view = LoginView.as_view(
    template_name="accounts/login_form.html"
)

logout_view = LogoutView.as_view(next_page='/')


# class ProfileCreateView(LoginRequiredMixin, CreateView):
#     model = Profile
#     form_class = ProfileForm

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         messages.success(self.request, '프로필이 생성되었습니다.')
#         return super().form_valid(form)
    


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "accounts/profile_edit.html"
    context_object_name = "profile"
    success_url = "/" # 확인

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        if created:
            messages.info(self.request, '프로필이 생성되었습니다.')
        return profile
        
    def form_valid(self, form):
        if form.cleaned_data.get('use_default_image'):
            if self.object.upload_img:  # 기존 업로드된 이미지 삭제 할 때
                self.object.upload_img.delete()
                        
            self.object.upload_img = None
        
        messages.success(self.request, '프로필이 수정되었습니다.')
        return super().form_valid(form)