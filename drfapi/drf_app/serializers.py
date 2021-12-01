
from rest_framework import serializers
from .models import Article, Author



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email', 'created_at', 'updated_at']



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'created_at', 'updated_at']

