from rest_framework.test import APITestCase, APIClient
from datetime import datetime

from authentication.factories import CustomUserFactory
from articles.factories import ArticleFactory


class TestArticle(APITestCase):
    def setUp(self) -> None:
        self.test_person_is_admin = CustomUserFactory(is_staff=True)
        self.test_person_just_user = CustomUserFactory()

        self.article1 = ArticleFactory(title="article1")
        self.article2 = ArticleFactory(title="article2")

    def test_get_all_articles_unauthorized(self):
        response = self.client.get("/api/articles/")
        self.assertEqual(200, response.status_code)

    def test_get_all_articles_authorized_just_user(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.get("/api/articles/")
        self.assertEqual(200, response.status_code)

    def test_get_all_articles_authorized_admin(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response = self.client.get("/api/articles/")
        self.assertEqual(200, response.status_code)

    def test_get_article_not_exists(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response = self.client.get("/api/articles/20000/")
        self.assertEqual(404, response.status_code)

    def test_get_article_1(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response_get = self.client.get("/api/articles/")
        list_of_articles = response_get.data
        article_for_get = list_of_articles[0]
        response = self.client.get(path=f"/api/articles/{article_for_get['id']}/")
        self.assertEqual(200, response.status_code)

    def test_create_article_unauthorized(self):
        response = self.client.post(
            path="/api/articles/",
            data={
                "title": "health",
                "content": "article about health",
                "date_of_publishing": datetime.now,
                "authors": "John Smith",
                "description": "good article",
            },
        )
        self.assertEqual(401, response.status_code)

    def test_create_article_just_user(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.post(
            path="/api/articles/",
            data={
                "title": "health",
                "content": "article about health",
                "date_of_publishing": "2007-01-01",
                "authors": "John Smith",
                "description": "good article",
            },
        )
        self.assertEqual(403, response.status_code)

    def test_create_article_is_admin(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response = self.client.post(
            path="/api/articles/",
            data={
                "title": "health",
                "content": "article about health",
                "date_of_publishing": "2007-01-01",
                "authors": "John Smith",
                "description": "good article",
            },
        )
        self.assertEqual(201, response.status_code)

    def test_put_article_unauthorized(self):
        response = self.client.put(
            path="/api/articles/1/",
            data={
                "title": "Gastro",
                "content": "article about gastro",
                "date_of_publishing": datetime.now,
                "authors": "John Smith",
                "description": "good article about gastro",
            },
        )
        self.assertEqual(401, response.status_code)

    def test_put_article_just_user(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.put(
            path="/api/articles/1/",
            data={
                "title": "Gastro",
                "content": "article about gastro",
                "date_of_publishing": datetime.now,
                "authors": "John Smith",
                "description": "good article about gastro",
            },
        )
        self.assertEqual(403, response.status_code)

    def test_put_article_is_admin(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response_get = self.client.get("/api/articles/")
        list_of_articles = response_get.data
        article_for_put = list_of_articles[0]
        response = self.client.put(
            path=f"/api/articles/{article_for_put['id']}/",
            data={
                "title": "Gastro",
                "content": "article about gastro",
                "date_of_publishing": "2007-01-01",
                "authors": "John Smith",
                "description": "good article about gastro",
            },
        )
        self.assertEqual(200, response.status_code)

    def test_patch_article_unauthorized(self):
        response = self.client.patch(path="/api/articles/2/", data={"title": "wine"})
        self.assertEqual(401, response.status_code)

    def test_patch_article_just_user(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.patch(path="/api/articles/2/", data={"title": "wine"})
        self.assertEqual(403, response.status_code)

    def test_patch_article_is_admin(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response_get = self.client.get("/api/articles/")
        list_of_articles = response_get.data
        article_for_patch = list_of_articles[0]
        response = self.client.patch(
            path=f"/api/articles/{article_for_patch['id']}/", data={"title": "Sport"}
        )
        self.assertEqual(200, response.status_code)

    def test_delete_article_unauthorized(self):
        response = self.client.delete(path="/api/articles/1/")
        self.assertEqual(401, response.status_code)

    def test_delete_article_just_user(self):
        self.client.force_authenticate(self.test_person_just_user)
        response = self.client.delete(path="/api/articles/1/")
        self.assertEqual(403, response.status_code)

    def test_delete_article_is_admin(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response_get = self.client.get("/api/articles/")
        list_of_articles = response_get.data
        article_for_delete = list_of_articles[0]
        response = self.client.delete(path=f"/api/articles/{article_for_delete['id']}/")
        self.assertEqual(204, response.status_code)

    def test_delete_articles_not_exists_is_staff(self):
        self.client.force_authenticate(self.test_person_is_admin)
        response = self.client.delete(path=f"/api/articles/20000/")
        self.assertEqual(404, response.status_code)
