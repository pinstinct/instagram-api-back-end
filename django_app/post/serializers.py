from rest_framework import serializers

from post.models import Post, PostPhoto


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'author',
            'created_date',
        )
        read_only_fields = (
            'created_date',
        )


# class PostPhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostPhoto
