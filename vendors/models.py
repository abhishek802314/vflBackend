from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class Vendor(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    products = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    phone = PhoneNumberField()
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    