from django.urls import include, path, re_path
from .views import ArticleList, ArticlesDetail

app_name = "articles"

urlpatterns = [
    path("articles/", ArticleList.as_view(), name="article-list"),
    path("articles/<pk>/", ArticlesDetail.as_view(), name="article-detail"),
]
