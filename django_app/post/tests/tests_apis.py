import os
import random

from django.contrib.auth import get_user_model
from django.urls import NoReverseMatch
from django.urls import resolve
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APILiveServerTestCase

from post.models import Post
from utils.testcase import APITestCaseAuthMixin

User = get_user_model()


class PostTest(APITestCaseAuthMixin, APILiveServerTestCase):
    def create_post(self, num=1):
        """
        :param num: 생성할 Post 수
        :return: num == 1일 경우 생성 요청의 response
        """
        url = reverse('api:post-list')
        # Post를 생성하는 API주소에 POST요청, response를 받아옴
        for i in range(num):
            response = self.client.post(url)
            if num == 1:
                return response

    def test_apis_url_exists(self):
        try:
            # PostList
            resolve('/api/post/')
            # PostDetail
            resolve('/api/post/1/')
        except NoReverseMatch as e:
            self.fail(e)

    def test_post_create(self):
        user = self.create_user()
        self.client.login(
            username=self.test_username,
            password=self.test_password
        )

        response = self.create_post()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # response의 key값 검사
        self.assertIn('author', response.data)
        self.assertIn('created_date', response.data)
        self.assertIn('photo_list', response.data)

        # response의 author 값 검사
        response_author = response.data['author']
        self.assertIn('pk', response_author)
        self.assertIn('username', response_author)

        # response의 postphoto_set 값 검사
        response_photo_list = response.data['photo_list']
        self.assertIsInstance(response_photo_list, list)
        for photo_object in response_photo_list:
            self.assertIn('pk', photo_object)
            self.assertIn('photo', photo_object)
            self.assertIn('created_date', photo_object)

        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.author.id, user.id)

    def test_cannot_create_post_not_authenticated(self):
        url = reverse('api:post-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.exists(), False)

    def test_post_list(self):
        self.create_user_and_login(self.client)

        num = random.randrange(1, 50)
        self.create_post(num)

        url = reverse('api:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # num 만큼 생성되었는지 확인
        self.assertEqual(len(response.data), num)

        # 생성된 response의 author 필드가 pk가 아닌 dict 형태로 전달되는지 확인
        # print(response.data)
        for item in response.data:
            # print(item)
            self.assertIn('author', item)
            item_author = item['author']
            # print(item_author)
            self.assertIn('pk', item_author)
            self.assertIn('username', item_author)

        # response의 postphoto_set 값 검사
        # ite = response.data['postphoto_set']
        # self.assertIsInstance(ite, list)
        # for postphoto_object in ite:
        #     self.assertIn('pk', postphoto_object)
        #     self.assertIn('photo', postphoto_object)
        #     self.assertIn('created_date', postphoto_object)

    def test_post_update_partial(self):
        pass

    def test_post_update(self):
        pass

    def test_post_retrieve(self):
        pass

    def test_post_destroy(self):
        pass


class PostPhotoTest(APITestCaseAuthMixin, APILiveServerTestCase):
    def test_photo_add_to_post(self):
        # 유저생성 및 로그인
        user = self.create_user_and_login(self.client)

        # 해당 유저로 Post 생성
        url = reverse('api:post-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.author, user)

        # 생성한 Post에 PostPhoto를 추가
        url = reverse('api:photo-create')

        # test_images.jpg 파일을 이용해서 생성
        file_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        # rb : 바이너리 모드로 읽기
        with open(file_path, 'rb') as fp:
            data = {
                'post': post.id,
                'photo': fp
            }
            response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('post', response.data)
        self.assertIn('photo', response.data)

        self.assertEqual(post.pk, response.data['post'])

    def test_cannot_photo_add_to_post_not_authenticated(self):
        pass

    def test_cannot_photo_add_to_post_user_is_not_author(self):
        pass
