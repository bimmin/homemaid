from django.test import TestCase

from ..forms import MaidForm


class TestMaidForm(TestCase):
    def test_form_should_have_defined_fields(self):
        form = MaidForm()

        assert 'name' in form.fields
        assert len(form.fields) == 1
