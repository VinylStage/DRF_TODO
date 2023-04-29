from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializer import ArticleSerializer, ArticleCreateSerializer, ArticleDetailSerializer
from users.models import User


class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        serializer = ArticleDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = get_object_or_404(Article, id=pk)
        if request.user == article.user:
            article.delete()
            return Response("deleted", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("You don't have any permission", status=status.HTTP_403_FORBIDDEN)
