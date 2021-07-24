from rest_framework import serializers

from posts.models import Post, Group, Comment, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'group', 'comments', 'pub_date')
        read_only_fields = ('author',)
