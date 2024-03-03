from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer



class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)


    def update(self, request, *args, **kwargs):

        instance = self.get_object()

        if instance.author != request.user:

            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):

        instance = self.get_object()

        if instance.author != request.user:

            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()

        if instance.author != request.user:

            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupViewSet(ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        raise MethodNotAllowed(request.method)


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_object(self):

        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')

        return get_object_or_404(self.get_queryset(), id=comment_id, post_id=post_id)
    

    def retrieve(self, request, *args, **kwargs):

        queryset = self.get_queryset()

        post_id = kwargs.get('post_id')
        comment_id = kwargs.get('comment_id')

        comment = get_object_or_404(queryset, post_id=post_id, comment_id=comment_id)

        if comment.author != request.user:

            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(comment)

        return Response(serializer.data)


    def update(self, request, *args, **kwargs):

        instance = self.get_object()

        if instance.author != request.user:

            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):

        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if instance.author != request.user:

            return Response(status=status.HTTP_403_FORBIDDEN)
        else:

            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):

        instance = self.get_object()

        if instance.author != request.user:

            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
