from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserList(models.Model):
    first_name = models.CharField(max_length=264, default="Your first name")
    last_name = models.CharField(max_length=264, default="Your last name")
    email = models.EmailField(max_length=254, default='XXX@123.com')
    phone = PhoneNumberField(region="CA", blank=True)
    role = models.BooleanField(default=True)

    def __str__(self):
        return "%s" %(self.first_name)