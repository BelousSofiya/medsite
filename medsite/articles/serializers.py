# from collections import defaultdict
# from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import Article

class ArticleSerializer((serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"