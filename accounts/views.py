from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

# 회원가입 기능
def register(request):
    if request.method == "GET":
        form = RegisterForm()

    else:
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user) # 자동 로그인 처리
            return redirect("/")

    return render(request, "accounts/register_form.html", {
        "form": form,
    })



# 로그인/로그아웃
login = LoginView.as_view(
    template_name="accounts/login_form.html"
)

logout = LogoutView.as_view(next_page='/')