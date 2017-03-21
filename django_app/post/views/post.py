"""
Class-based view로
PostList, PostDetail, PostCreate, PostDelete 뷰를 작성
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from post.forms import PostForm
from post.models import Post, PostComment
from post.models import PostPhoto

__all__ = (
    'PostList',
    'PostDetail',
    'PostDelete',
    'PostCreate',
)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post


class PostCreate(View):
    form_class = PostForm
    template_name = 'post/post_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request.FILES)
        author = request.user
        post = Post.objects.create(author=author)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data.get('content', '').strip()
            if content != '':
                PostComment.objects.create(
                    post=post,
                    author=author,
                    content=content
                )
            for file in request.FILES.getlist('photos'):
                PostPhoto.objects.create(
                    post=post,
                    photo=file
                )

            return redirect('post:post-list')
        else:
            return HttpResponse(form.errors)


class PostDelete(View):
    pass
