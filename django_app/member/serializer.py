from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            # 'id',
            'username',
            # 'first_name',
            # 'last_name',
            # 'email',
            # 'is_staff',
            # 'groups',
        )
