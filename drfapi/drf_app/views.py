
from drf_app.models import Article, Author
from drf_app.serializers import ArticleSerializer, AuthorSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET'])
def get_articles(request, format=None):
    """
    Get all articles
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_article(request, format=None):
    """
    Create a new article.
    """
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def one_article(request, pk, format=None):
    """
    Retrieve, update or delete a specific Article.
    """
    try:
        article = Article.objects.get(pk=pk) #pk comes from the url
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def get_authors(request, format=None):
    """
    Get all articles
    """
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_author(request, format=None):
    """
    Create a new article.
    """
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def one_author(request, pk, format=None):
    """
    Retrieve, update or delete a specific Author.
    """
    try:
        author = Author.objects.get(pk=pk) #pk comes from the url
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)