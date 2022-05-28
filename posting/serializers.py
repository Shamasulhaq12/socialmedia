from rest_framework import serializers
from .models import Post, Media, Comment, Like


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    post_medias = MediaSerializer(read_only=True, many=True)
    post_likes = LikeSerializer(read_only=True, many=True)
    post_comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'
