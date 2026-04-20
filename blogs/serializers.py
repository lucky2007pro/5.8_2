from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    blog = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

class BlogModelSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'user', 'created_at', 'updated_at', 'comments']

class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'content', 'created_at', 'updated_at']
