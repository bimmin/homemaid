from datetime import date

from django.test import TestCase

from ..models import Maid
from ..serializer import MaidSerializer


class TestMaidSerializer(TestCase):
    def test_serializer_should_serialize_object_to_json(self):
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
        maids = Maid.objects.all()
        serializer = MaidSerializer(maids, many=True)

        #Then
        assert serializer.data == [{'id': 1, 'name': 'Bimmin'}, {'id': 2,'name':'Bb'}]