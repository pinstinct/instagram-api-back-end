from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from post.models import Post, PostPhoto

User = get_user_model()


def post_list(request):
    """
    JsonResponse를 이용해서 Post.objects.all()에 해당하는 객체 리스트를 리턴
    """
    # post_list = Post.objects.all()
    # 이 방법이 더 효율적임
    # post_list = Post.objects.select_related('author')
    # post_dict_list = []
    #
    # # 전체 Post를 loop
    # for post in post_list:
    #     cur_post_dict = {
    #         'pk': post.pk,
    #         'photo_list': [],
    #         'created_date': post.created_date,
    #         'author': {
    #             'pk': post.author.pk,
    #             'username': post.author.username,
    #         }
    #     }
    #     photo_list = post.postphoto_set.all()
    #     for post_photo in photo_list:
    #         photo_dict = {
    #             'pk': post_photo.pk,
    #             'photo': post_photo.photo.url,
    #         }
    #         cur_post_dict['photo_list'].append(photo_dict)
    #     post_dict_list.append(cur_post_dict)

    context = {
        # 'post_list': post_dict_list
        'post_list': [post.to_dict() for post in Post.objects.select_related()]
    }
    return JsonResponse(data=context)


@csrf_exempt
def post_create(request):
    """
    request.POST로 전달된 author_id를 받아 새 post를 생성
    이후 생성된 post의 id 값을 Httpresponse로 반환

    받은 author_id에 해당하는 MyUser 객체를 가져옴
    실패시 예외처리로 주어진 author_id에 해당하는 User는 없음을 리턴

    urls.py에 연결
    """
    if request.method == 'POST':
        try:
            author_id = request.POST['author_id']
            author = User.objects.get(id=author_id)

        except KeyError:
            return HttpResponse('key "author_id" is required field')
        except User.DoesNotExist:
            return HttpResponse('author_id {} is not exist'.format(
                request.POST['author_id']
            ))
        post = Post.objects.create(author=author)
        return HttpResponse('{}'.format(post.pk))

    else:
        return HttpResponse('Post create view')


@csrf_exempt
def post_photo_add(request):
    if request.method == 'POST':
        try:
            post_id = request.POST['post_id']
            photo = request.FILES['photo']
            post = Post.objects.get(id=post_id)
        except KeyError:
            return HttpResponse('post_id and photo is required field')
        except Post.DoesNotExist:
            return HttpResponse('post_id {} is not exist'.format(
                request.POST['post_id']
            ))
        PostPhoto.objects.create(
            post=post,
            photo=photo
        )
        return HttpResponse('Post: {}, PhotoList: {}'.format(
            post.id,
            [photo.id for photo in post.postphoto_set.all()]
        ))
    else:
        return HttpResponse('Post photo add view')
