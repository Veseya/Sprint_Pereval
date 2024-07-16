import json
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Pereval, Users, Coords, Level
from .serializers import PerevalSerializer


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            status="",
            beauty_title="Тест_1",
            title="Пхия_1",
            other_titles="Триев_1",
            connect="",
            add_time="",
            tourist_id=Users.objects.create(
                email="test_1@mail.ru",
                last_name="Петров",
                first_name="Петр",
                patronymic="Петрович",
                phone="+7 111 11 55"
            ),
            coord_id=Coords.objects.create(
                latitude=40.3842,
                longitude=10.1525,
                height=1100
            ),
            level=Level.objects.create(
                summer_lev="1A",
                autumn_lev="1A",
                winter_lev="1A",
                spring_lev="1A"
            ),
        )

        self.pereval_2 = Pereval.objects.create(
            status="",
            beauty_title="Тест_2",
            title="Пхия_2",
            other_titles="Триев_2",
            connect="",
            add_time="",
            tourist_id=Users.objects.create(
                email="test_2@mail.ru",
                last_name="Сидоров",
                first_name="Василий",
                patronymic="Сидорович",
                phone="+7 222 22 55"
            ),
            coord_id=Coords.objects.create(
                latitude=50.3842,
                longitude=15.1525,
                height=950
            ),
            level=Level.objects.create(
                summer_lev="1A",
                autumn_lev="1A",
                winter_lev="1A",
                spring_lev="1A"
            ),
        )

    def test_get(self):
        url = reverse('pereval-list')
        resource = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data

        self.assertEqual(serializer_data, resource.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, resource.status_code)

    def test_get_detail(self):
        url = reverse('pereval-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_user_update(self):
        url = reverse("pereval-detail", args=(self.pereval_1.id,))
        data = {
                'id': 1,
                "status": "",
                "beauty_title": "Тест_1",
                "title": "Пхия_1",
                "other_titles": "Триев_1",
                "connect": "",
                "add_time": self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                "tourist_id": {
                    "email": "test_1@mail.ru",
                    "last_name": "Иванов",
                    "first_name": "Федор",
                    "patronymic": "Николаевич",
                    "phone": "+7 111 11 55"
                },
                "coord_id": {
                    "latitude": 57.3842,
                    "longitude": 18.1525,
                    "height": 1215
                },
                "level": {
                    "summer_lev": "1A",
                    "autumn_lev": "1A",
                    "winter_lev": "1A",
                    "spring_lev": "1A"
                },
                "images": [
                 ]
            },
        json_data = json.dumps(data)
        response = self.client.patch(path=url, content_type='application/json', data=json_data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.pereval_1.refresh_from_db()
        self.assertEquals("test_1@mail.ru", self.pereval_1.tourist_id.email)
        self.assertEquals("Петров", self.pereval_1.tourist_id.last_name)
        self.assertEquals("Петр", self.pereval_1.tourist_id.first_name)
        self.assertEquals("Петрович", self.pereval_1.tourist_id.patronymic)


class PrevalSerializerTestCase(TestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            id=1,
            status="",
            beauty_title="Тест_1",
            title="Пхия_1",
            other_titles="Триев_1",
            connect="",
            add_time="",
            tourist_id=Users.objects.create(
                email="test_1@mail.ru",
                last_name="Петров",
                first_name="Петр",
                patronymic="Петрович",
                phone="+7 111 11 55"
            ),
            coord_id=Coords.objects.create(
                latitude=40.3842,
                longitude=10.1525,
                height=1100
            ),
            level=Level.objects.create(
                summer_lev="1A",
                autumn_lev="1A",
                winter_lev="1A",
                spring_lev="1A"
            ),
        )

        self.pereval_2 = Pereval.objects.create(
            id=2,
            status="",
            beauty_title="Тест_2",
            title="Пхия_2",
            other_titles="Триев_2",
            connect="",
            add_time="",
            tourist_id=Users.objects.create(
                email="test_2@mail.ru",
                last_name="Сидоров",
                first_name="Василий",
                patronymic="Сидорович",
                phone="+7 222 22 55"
            ),
            coord_id=Coords.objects.create(
                latitude=50.3842,
                longitude=15.1525,
                height=950
            ),
            level=Level.objects.create(
                summer_lev="1A",
                autumn_lev="1A",
                winter_lev="1A",
                spring_lev="1A"
            ),
        )

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        expected_data = [
            {
                'id': 1,
                "status": "",
                "beauty_title": "Тест_1",
                "title": "Пхия_1",
                "other_titles": "Триев_1",
                "connect": "",
                "add_time": self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                "tourist_id": {
                    "email": "test_1@mail.ru",
                    "last_name": "Петров",
                    "first_name": "Петр",
                    "patronymic": "Петрович",
                    "phone": "+7 111 11 55"
                },
                "coord_id": {
                    "latitude": 40.3842,
                    "longitude": 10.1525,
                    "height": 1100
                },
                "level": {
                    "summer_lev": "1A",
                    "autumn_lev": "1A",
                    "winter_lev": "1A",
                    "spring_lev": "1A"
                },
                "images": [
                 ]
            },

            {
                'id': 2,
                "status": "",
                "beauty_title": "Тест_2",
                "title": "Пхия_2",
                "other_titles": "Триев_2",
                "connect": "",
                "add_time": self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                "tourist_id": {
                    "email": "test_2@mail.ru",
                    "last_name": "Сидоров",
                    "first_name": "Василий",
                    "patronymic": "Сидорович",
                    "phone": "+7 222 22 55"
                },
                "coord_id": {
                    "latitude": 50.3842,
                    "longitude": 15.1525,
                    "height": 950
                },
                "level": {
                    "summer_lev": "1A",
                    "autumn_lev": "1A",
                    "winter_lev": "1A",
                    "spring_lev": "1A"
                },
                "images": [
                ]
            },
        ]
        self.assertEqual(serializer_data, expected_data)
