from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.db import transaction

# 회원가입 기능 : CBV로 변경하자
def register(request):  # 여기서부터 다시 공부 ---------------
    if request.method == "GET":
        user_form = RegisterForm()
        profile_form = ProfileForm() 
    else:
        user_form = RegisterForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                # User 저장
                user = user_form.save()
                # Profile 저장
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                # 자동 로그인
                login(request, user)
                return redirect("/")

    return render(request, "accounts/register_form.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })



# 로그인/로그아웃
login = LoginView.as_view(
    template_name="accounts/login_form.html"
)

logout = LogoutView.as_view(next_page='/')