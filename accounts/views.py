from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 회원가입 기능
def register(request):
    if request.method == "GET":
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()

            # login(request, user) # 자동 로그인 처리할 때

            return redirect("/") # 회원가입 후 자동 로그인이 되고 메인으로 가면 좋겠다.

    return render(request, "accounts/register_form.html", {
        "form": form,
    })