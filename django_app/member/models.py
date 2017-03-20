from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    # username = models.CharField(max_length=100)
    relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relationship',
        related_name='relation_user_set'
    )

    def to_dict(self):
        ret = {
            'pk': self.pk,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
        return ret

    def follow(self, user, type):
        """
        이미 follow한 사람일 경우 안되도록 unique_together를 설정 (Relationship)
        상대방이 나를 block했을 경우 raise Exception(msg)

        :param user:
        :param type:
        :return:
        """
        self.relations_from_user.create(
            to_user=user,
            relation_type=Relationship.TYPE_FOLLOW
        )

    def block(self, user):
        pass

    @property
    def following(self):
        relations = self.relations_from_user.filter(
            relation_type=Relationship.TYPE_FOLLOW
        )
        return MyUser.objects.filter(id__in=relations.values('to_user_id'))

    @property
    def followers(self):
        pass

    @property
    def block_user(self):
        pass

    def friends(self):
        pass

        # def remove_relationship(self, user, type):
        #     Relationship.objects.filter(
        #         from_user=self,
        #         to_user=user,
        #         type=type
        #     ).delete()
        #     return
        #
        # def get_relationships(self, type):
        #     return self.relation.filter(
        #         to_user__type=type,
        #         to_user__from_user=self
        #     )
        #
        # def get_related_to(self, type):
        #     return self.relation_user_set.filter(
        #         from_user__type=type,
        #         from_user__to_user=self
        #     )
        #
        # @property
        # def get_following(self):
        #     return self.get_relationships(TYPE_FOLLOW)
        #
        # @property
        # def get_followers(self):
        #     return self.get_related_to(TYPE_FOLLOW)
        #
        # @property
        # def get_friends(self):
        #     return self.relationship.filter(
        #         to_user__type=TYPE_FOLLOW,
        #         to_user__from_user=self,
        #         from_user__type=TYPE_FOLLOW,
        #         from_user__to_user=self,
        #     )


class Relationship(models.Model):
    TYPE_FOLLOW = 'f'
    TYPE_BLOCK = 'b'
    RELATIONSHIP_STATUS = (
        (TYPE_FOLLOW, 'Following'),
        (TYPE_BLOCK, 'Blocked')
    )

    from_user = models.ForeignKey(MyUser, related_name='relations_from_user')
    to_user = models.ForeignKey(MyUser, related_name='relations_to_user')
    relation_type = models.CharField(max_length=1, choices=RELATIONSHIP_STATUS, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Relation({}) From({}) To({})'.format(
            self.get_relation_type_display(),
            self.from_user.username,
            self.to_user.username,
        )
