from rest_framework import serializers

from member.serializer import UserSerializer
from post.models import Post
from post.serializer.post_photo import PostPhotoSerializer

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    postphoto_set = PostPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
            'postphoto_set',
        )
        read_only_fields = (
            'author',
            'created_date',
        )
