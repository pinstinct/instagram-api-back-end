from rest_framework import serializers

from member.serializer import UserSerializer
from post.models import Post

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
        )
        read_only_fields = (
            'author',
            'created_date',
        )
        # depth = 1
