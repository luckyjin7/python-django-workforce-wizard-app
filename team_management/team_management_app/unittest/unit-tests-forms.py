import unittest
from django import forms
from models import UserList
from forms import ListForm

class ListFormTest(unittest.TestCase):
    def test_form_fields(self):
        form = ListForm()
        self.assertIsInstance(form, forms.ModelForm)
        self.assertEqual(form.Meta.model, UserList)
        self.assertEqual(form.Meta.fields, "__all__")