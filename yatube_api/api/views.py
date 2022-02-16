from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthor, IsAuthorOrReadOnlyPermission
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer,
)

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnlyPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        new_queryset = post.comments
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$following__username',)
    permission_classes = (permissions.IsAuthenticated, IsAuthor,)

    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        queryset = user.follower.all()
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        following_username = self.request.data['following']
        following = User.objects.get(username=following_username)
        serializer.save(user=user, following=following)
