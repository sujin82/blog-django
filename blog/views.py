from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView   # CBV 방식
from django.urls import reverse
from .models import Post
from .forms import PostForm


# 메인 뷰 : TemplateView로 시작해서 기능을 추가하면서 커스텀 뷰 클래스로 전환 계획
main_page = TemplateView.as_view(
    template_name='index.html'
)

# 블로그 게시글 목록
post_list = ListView.as_view(
    model=Post
)


# 블로그 게시글 상세
post_detail = DetailView.as_view(
    model=Post,
)


# 블로그 글쓰기
post_write = CreateView.as_view(
    model=Post,
    form_class=PostForm,
    template_name="blog/post_write.html",
    success_url="/blog/",  
)


# 블로그 글 수정하기
post_edit = UpdateView.as_view(
    model=Post,
    form_class=PostForm,
    template_name="blog/post_edit.html",
    success_url="/blog/", # 동적으로 변경(수정후에는 상세가 보이게)
)


# 블로그 글 삭제 :: 테스트를 위해 post_confirm_delete.html 페이지로 생성했지만 js의 confirm()이나 모달 팝업으로 대체할 예정
post_delete = DeleteView.as_view(
    model=Post,
    success_url="/blog/",
)


# 게시글 검색 기능
post_search = ListView.as_view(
    model=Post,
    
)