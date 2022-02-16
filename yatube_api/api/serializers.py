from posts.models import Comment, Follow, Group, Post
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    #user = SlugRelatedField(slug_field='username', read_only='True')
    #following = SlugRelatedField(slug_field='username', read_only='True')

    class Meta:
        model = Follow
        fields = ('__all__')
#        fields = ('user', 'following')
