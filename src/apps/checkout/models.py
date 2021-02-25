from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.fields import BooleanField
from phonenumber_field.modelfields import PhoneNumberField

MAX_LENGTH: int = 30
# Create your models here.


class PageOptions(models.Model):
    professions = ArrayField(
        models.CharField(max_length=MAX_LENGTH), default=list
    )
    profile_image = models.CharField(max_length=MAX_LENGTH)

    # review_name = models.CharField(max_length=MAX_LENGTH)
    # review_image = models.CharField(max_length=MAX_LENGTH)
    # review_quote = models.CharField(max_length=MAX_LENGTH)

    # portfolio_image = models.CharField(max_length=MAX_LENGTH)
    # portfolio_description = models.CharField(max_length=900)


class ContactOptions(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    phone_number = PhoneNumberField()
    whatsapp = BooleanField()
    messenger = models.CharField(max_length=MAX_LENGTH, null=True, blank=True)

    class Meta:
        verbose_name = "Contact Option"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class CheckoutOptions(models.Model):
#     """
#     Required Fields to customize the users product.
#     """

#     class Meta:
#         verbose_name = "Checkout Option"

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# TODO:
# Position that increments, and can be overidden
class Stage(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    # position = models.AutoField()
