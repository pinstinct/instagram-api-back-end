import time
from rest_framework import generics
from rest_framework import permissions

from post.models import Post
from post.serializer import PostSerializer
from utils.pagination import PostPagination

__all__ = (
    'PostList',
    'PostDetail',
)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        time.sleep(2)
        return super().list(request, *args, **kwargs)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
