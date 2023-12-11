from django.test import TestCase
from models import UserList

class UserListTestCase(TestCase):
    def test_string_representation(self):
        user = UserList(first_name="John")
        self.assertEqual(str(user), "John")

    def test_default_first_name(self):
        user = UserList()
        self.assertEqual(user.first_name, "Your first name")

    def test_default_last_name(self):
        user = UserList()
        self.assertEqual(user.last_name, "Your last name")

    def test_default_email(self):
        user = UserList()
        self.assertEqual(user.email, "XXX@123.com")

    def test_default_phone(self):
        user = UserList()
        self.assertEqual(user.phone.region, "CA")
        self.assertTrue(user.phone.blank)

    def test_default_role(self):
        user = UserList()
        self.assertTrue(user.role)