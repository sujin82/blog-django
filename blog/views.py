# from django.shortcuts import render # FBV 방식
from django.views.generic import ListView, DetailView, TemplateView   # CBV 방식
from .models import Post

# 메인 뷰 : TemplateView로 시작해서 기능을 추가하면서 커스텀 뷰 클래스로 전환 계획
main_page = TemplateView.as_view(
    template_name='index.html'
)

# 블로그의 모든 포스트 목록 뷰
post_list = ListView.as_view(
    model=Post
)


# 블로그의 상세 조회(단건) 뷰
post_detail = DetailView.as_view(
    model=Post,
)