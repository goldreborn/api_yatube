from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from .permissions import OwnershipPermission
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, OwnershipPermission]

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, OwnershipPermission]

    def get_queryset(self) -> Comment:
        return get_object_or_404(
            Post, id=self.kwargs.get('post_id')
        ).comments.all()

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(
            author=self.request.user, post=get_object_or_404(
                Post, id=self.kwargs['post_id']
            )
        )
