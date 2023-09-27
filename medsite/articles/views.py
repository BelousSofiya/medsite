from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import Article
from .serializers import ArticleSerializer
from .permissions import ReadOnly


class ArticleList(ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (ReadOnly | IsAdminUser,)
    queryset = Article.objects.all()


class ArticlesDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (ReadOnly | IsAdminUser,)
    queryset = Article.objects.all()
