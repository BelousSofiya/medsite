import factory.django

from .models import CustomUser

class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
        django_get_or_create = ('email',)

    email = factory.Sequence(lambda n: f"test@test{n + 1}.com")
    name = factory.Sequence(lambda n: f"Test_person_name{n + 1}")
    surname = factory.Sequence(lambda n: f"Test_person_surname{n + 1}")
    password = ''
