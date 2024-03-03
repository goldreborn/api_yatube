
from rest_framework.serializers import (
    ModelSerializer, SlugRelatedField, PrimaryKeyRelatedField
)


from posts.models import Post, Comment, Group


class CommentSerializer(ModelSerializer):
    
    post = PrimaryKeyRelatedField(read_only=True)
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:

        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class PostSerializer(ModelSerializer):

    group = PrimaryKeyRelatedField(
        required=False,
        queryset=Group.objects.all()
    )
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:

        model = Post
        fields = '__all__'


class GroupSerializer(ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:

        model = Group
        fields = '__all__'
