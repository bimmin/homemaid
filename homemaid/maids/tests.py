import os
from datetime import date
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from .models import Maid


class TestMaid(TestCase):
    def test_model_should_have_defined_fields(self):
        #Given
        Maid.objects.create(
            name='Bimmin',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the year',
            cartificate='Best Maid 2020',
            salary=3000
        )

        #When
        maid = Maid.objects.last()

        #Then
        self.assertEqual(maid.name, 'Bimmin')
        self.assertEqual(maid.birthdate, date(1998, 4, 29))
        self.assertEqual(maid.description, 'Super Maid of the year')
        self.assertEqual(maid.cartificate, 'Best Maid 2020')
        self.assertEqual(maid.salary, 3000)

    def test_model_should_have_image_field(self):
        #Given
        mock = MagicMock(spec=File)
        mock.name = 'profile.png'

        Maid.objects.create(
            name='Bimmin',
            profile_image=mock,
            birthdate=date(1998, 4, 29),
            description='Super Maid of the year',
            cartificate='Best Maid 2020',
            salary=3000
        )

        #When
        maid = Maid.objects.last()

        #Then
        self.assertEqual(maid.profile_image.name, 'profile.png')

        os.remove('profile.png')
