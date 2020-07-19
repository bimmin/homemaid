from datetime import date
from django.test import TestCase
from django.urls import reverse

from ..models import Maid


class TestMaidListView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-list'))
        assert response.status_code == 200

    def test_view_should_display_maid_list(self):
        #Given
        Maid.objects.create(
            name='Bimmin',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the year',
            cartificate='Best Maid 2020',
            salary=3000
        )
        Maid.objects.create(
            name='Bb',
            birthdate=date(1998, 9, 30),
            description='Ultra Maid of the year',
            cartificate='Best Maid 2022',
            salary=3200
        )

        #When
        response = self.client.get(reverse('maid-list'))

        #Then
        assert '<li>Bimmin</li>' in str(response.content)
        assert '<li>Bb</li>' in str(response.content)


class TestMaidListAnotherView(TestCase):
    def test_view_should_display_maid_list(self):
        response = self.client.get(reverse('maid-another-list'))
        assert response.status_code == 200
    

    def test_view_should_display_maid_list(self):
        #Given
        Maid.objects.create(
            name='Bimmin',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the year',
            cartificate='Best Maid 2020',
            salary=3000
        )
        Maid.objects.create(
            name='Bb',
            birthdate=date(1998, 9, 30),
            description='Ultra Maid of the year',
            cartificate='Best Maid 2022',
            salary=3200
        )

        #When
        response = self.client.get(reverse('maid-another-list'))

        #Then
        assert '<li>Bimmin</li>' in str(response.content)
        assert '<li>Bb</li>' in str(response.content)


class TestMaidAddView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-add'))
        assert response.status_code == 200

    def test_view_should_have_maid_form(self):
        response = self.client.get(reverse('maid-add'))
    
        assert '<form action="." method="POST">' in str(response.content)

        assert '<input type="hidden" name="csrfmiddlewaretoken"' in str(response.content)

        name_field = '<input type="text" name="name" maxlength="300" required id="id_name">'
        assert name_field in str(response.content)

        button = '<button class="btn btn-primary" type="submit">Submit</button>'
        assert button in str(response.content)