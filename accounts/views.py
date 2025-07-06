from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.contrib import messages

def register(request):
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