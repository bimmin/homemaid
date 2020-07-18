from django.test import TestCase
from django.urls import reverse


class TestMaidListView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-list'))
        assert response.status_code == 200
