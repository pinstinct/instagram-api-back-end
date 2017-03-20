"""
Class-based view로
PostList, PostDetail, PostCreate, PostDelete 뷰를 작성
"""
from django.shortcuts import render
from django.views import View

from post.models import Post

__all__ = (
    'PostList',
    'PostDetail',
    'PostDelete',
)


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'post/post_list.html', context)


class PostDetail(View):
    pass


class PostDelete(View):
    pass
