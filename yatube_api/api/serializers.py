
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from posts.models import Post, Comment, Group


class CommentSerializer(ModelSerializer):

    class Meta:

        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class PostSerializer(ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:

        model = Post
        fields = '__all__'


class GroupSerializer(ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:

        model = Group
        fields = '__all__'
