from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'group', 'pub_date')
        read_only_fields = ('author',)
