import json

from django.forms import model_to_dict
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from bot.models import WordBlackList
from bot.serializers.word_blacklist import WordBlackListSerializer


class WordBlackListViewsetTest(APITestCase):
    """
    class de test
    """

    @classmethod
    def setUpTestData(cls):
        WordBlackList.objects.create(words='tabarnak;lama')

    def setUp(self):
        self.client = APIClient()
        self.word_blacklist = WordBlackList.objects.last()

    def test_endpoint_list(self):
        url = reverse('wordblacklist-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        blacklist = json.loads(response.content)
        sure_blacklist = WordBlackListSerializer(model_to_dict(self.word_blacklist)).data
        self.assertEqual(blacklist, sure_blacklist)
