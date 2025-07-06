from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.http import JsonResponse
from blog.models import Post, Like, Comment
from blog.forms import PostForm, CommentForm



# 메인 뷰 : TemplateView로 시작해서 기능을 추가하면서 커스텀 뷰 클래스로 전환 계획
main_page = TemplateView.as_view(
    template_name='index.html'
)

# 블로그 게시글 목록
post_list = ListView.as_view(
    model=Post
)


# 블로그 게시글 상세
def post_detail(request, pk):   # CBV로 나중에 바꾸자
    post = get_object_or_404(Post, pk=pk)

    # 댓글 작성
    if request.method == "POST" and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                content=content,
                author=request.user,
                post=post
            )
            return redirect('blog:post_detail', pk=pk)
        

    # 조회수 증가
    viewed_posts = request.session.get('viewed_posts', [])
    is_viewed = pk in viewed_posts
    is_author = request.user.is_authenticated and request.user == post.author

    if not is_author and not is_viewed:
        post.view_count += 1
        post.save(update_fields=['view_count'])

        viewed_posts.append(pk)

        if len(viewed_posts) > 100:
            viewed_posts = viewed_posts[-100:]

        request.session['viewed_posts'] = viewed_posts
        request.session.modified = True
    
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    return render(request, 'blog/post_detail.html', {'post': post, 'comments':comments})



# 블로그 글쓰기
class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    form_class=PostForm
    template_name="blog/post_write.html"
    success_url="/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



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



# 블로그 글 삭제 :: ★ 테스트를 위해 post_confirm_delete.html 페이지로 생성했지만 js의 confirm()이나 모달 팝업으로 대체할 예정
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name="blog/post_detail.html"
    success_url="/blog/"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user




# 게시글 검색 기능(FBV) : 타이틀검색(검색 필드 폼 활용), 카테고리(탭 디자인)
class PostSearchView(ListView):
    pass
    




# 좋아요
class ToggleLikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)

        if request.user == post.author:
            return JsonResponse({
                'error': '본인이 작성한 게시글에는 좋아요를 누를 수 없어요.',
                'liked': False,
                'likes_count': post.like_set.count()
            }, status=400)
        
        has_liked = Like.objects.filter(
            user=request.user,
            post = post
        ).exists()
        
        if has_liked:
            Like.objects.filter(user=request.user, post=post).delete()
            liked = False
        else:
            Like.objects.create(user=request.user, post=post)
            liked = True
        
        return JsonResponse({
            'liked': liked,
            'likes_count': post.like_set.count()
        })
    


# 댓글 생성
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):  # kwargs = keyword arguments
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk})