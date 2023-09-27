import factory.fuzzy
from datetime import datetime

from .models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
        django_get_or_create = ('title',)

    title = factory.Sequence(lambda n: f"test_title {n}")
    content = factory.Sequence(lambda n: f"test_content {n}")
    source_link = factory.Sequence(lambda n: f"http://tect.com/test/{n}")
    date_of_publishing = datetime.now()
    # date_on_site = factory.Sequence(datetime.now)
    authors = factory.Sequence(lambda n: f"test_author {n}")
    description = factory.Sequence(lambda n: f"test_description {n}")


