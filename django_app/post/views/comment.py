from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from post.models import Post
from post.models import PostComment

__all__ = (
    'CommentCreate',
)


@method_decorator(login_required, name='dispatch')
class CommentCreate(CreateView):
    model = PostComment
    fields = (
        # 'author',
        # 'post',
        'content',
    )

    def get_success_url(self):
        return reverse('post:post-detail', kwargs={'pk': self.kwargs['post_pk']})

    def form_valid(self, form):
        comment = form.save(commit=False)
        post_pk = self.kwargs['post_pk']
        post = Post.objects.get(pk=post_pk)
        author = self.request.user
        comment.post = post
        comment.author = author
        comment.save()
        return HttpResponseRedirect(self.get_success_url())

        # def post(self, request, *args, **kwargs):
        #     post_pk = self.kwargs['post_pk']
        #     post = Post.objects.get(id=post_pk)
        #     content = request.POST['content']
        #     author = request.user
        #
        #     PostComment.objects.create(
        #         author=author,
        #         post=post,
        #         content=content,
        #     )
        #     return redirect('post:post-detail', kwargs={'pk': post_pk})
