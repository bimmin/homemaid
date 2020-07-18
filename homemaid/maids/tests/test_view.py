from django.test import TestCase


class TestMaidListView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get('/maids/')
        assert response.status_code == 200
