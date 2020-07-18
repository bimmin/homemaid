from django.contrib import admin
from django.test import TestCase

from ..admin import MaidAdmin
from ..models import Maid 


class MaidAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        assert isinstance(admin.site._registry[Maid], MaidAdmin)

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'birthdate',
            'description',
            'cartificate',
            'salary',
        )
        assert MaidAdmin.list_display == expected
