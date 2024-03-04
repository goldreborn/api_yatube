from rest_framework.serializers import (
    ModelSerializer, SlugRelatedField
)

from posts.models import Post, Comment, Group


class CommentSerializer(ModelSerializer):

    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:

        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class PostSerializer(ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:

        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'group')


class GroupSerializer(ModelSerializer):

    class Meta:

        model = Group
        fields = ('id', 'title', 'slug', 'description')
