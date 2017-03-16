from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from post.models import Post

User = get_user_model()


class PostTest(APILiveServerTestCase):
    test_username = 'test_username'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        return user

    def test_post_create(self):
        # Post를 만들 유저를 생성 및 로그인
        user = self.create_user()
        self.client.login(
            usernmae=self.test_username,
            password=self.test_password
        )

        url = reverse('post-create')
        # Post를 생성하는 API주소에 POST요청, response를 받아옴
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.author.id, user.id)

    def test_cannot_create_post_not_authenticated(self):
        url = reverse('post-create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.exists(), False)

    def test_post_list(self):
        pass

    def test_post_update_partial(self):
        pass

    def test_post_update(self):
        pass

    def test_post_retrieve(self):
        pass

    def test_post_destroy(self):
        pass
