from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    template_name="blog/post_detail.html",
    context_object_name="post"
)


# 블로그 글쓰기
class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    form_class=PostForm
    template_name="blog/post_write.html"
    success_url="/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

post_write = PostCreateView.as_view()



# 블로그 글 수정하기
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    form_class=PostForm
    template_name="blog/post_edit.html"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
    def get_success_url(self):
        return f"/blog/{self.object.pk}/"
    
    success_url="/blog/" # ★ 동적으로 변경(수정후에는 상세가 보이게)

post_edit = PostUpdateView.as_view()



# 블로그 글 삭제 :: ★ 테스트를 위해 post_confirm_delete.html 페이지로 생성했지만 js의 confirm()이나 모달 팝업으로 대체할 예정
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name="blog/post_detail.html"
    success_url="/blog/"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

post_delete = PostDeleteView.as_view()




# 게시글 검색 기능(FBV) : 타이틀검색(검색 필드 폼 활용), 카테고리(탭 디자인)
class PostSearchView(ListView):
    pass
    