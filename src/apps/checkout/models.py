from typing import Any, Optional
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import BooleanField, CharField
from phonenumber_field.modelfields import PhoneNumberField

MAX_LENGTH: int = 30
# Create your models here.


def create_model(name, fields: Optional[dict[CharField]] = None):

    if fields:
        return type(name, (models.Model,), fields)


# def create_profession_model() -> Any:
#         return create_model('Profession', {'Profession': name})


class Profession(models.Model):
    profession = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return str(self.profession)


class Portfolio(models.Model):
    file_name = models.CharField(max_length=MAX_LENGTH)
    # position = models.AutoField()
    alt = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return str(self.file_name)


class Review(models.Model):
    def __str__(self):
        return str(self.name)


class CheckoutOptions(models.Model):
    """
    Required Fields to customize the users product.
    """

    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    image = models.CharField(max_length=MAX_LENGTH)

    phone_number = PhoneNumberField()
    whatsapp = BooleanField()
    messenger = models.CharField(max_length=MAX_LENGTH, null=True)

    professions = ArrayField(models.CharField(max_length=MAX_LENGTH))

    custom_portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, blank=True, null=True
    )

    reviewers_name = models.CharField(max_length=MAX_LENGTH)
    reviewers_image = models.CharField(max_length=MAX_LENGTH)
    reviewers_quote = models.CharField(max_length=MAX_LENGTH)

    class Meta:
        verbose_name = "Checkout Option"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"