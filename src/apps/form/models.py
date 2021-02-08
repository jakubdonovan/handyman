from django.db import models
from django.db.models.fields import BooleanField
from phonenumber_field.modelfields import PhoneNumberField

MAX_LENGTH = 30
# Create your models here.


class ProfessionOption(models.Model):
    profession = models.CharField(max_length=MAX_LENGTH)


class Image(models.Model):
    file_name = models.CharField(max_length=MAX_LENGTH)
    # position = models.AutoField()
    alt = models.CharField(max_length=MAX_LENGTH)


class Portfolio(models.Model):
    file_name = models.CharField(max_length=MAX_LENGTH)
    # position = models.AutoField()
    alt = models.CharField(max_length=MAX_LENGTH)


class Review(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    image = models.CharField(max_length=MAX_LENGTH)
    quote = models.CharField(max_length=MAX_LENGTH)


class PageOptions(models.Model):
    professions = models.ForeignKey(ProfessionOption, on_delete=models.CASCADE)
    custom_portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    custom_reviews = models.ForeignKey(Review, on_delete=models.CASCADE)


class ContactOptions(models.Model):
    phone_number = PhoneNumberField()
    whatsapp = BooleanField()
    messenger = models.CharField(max_length=MAX_LENGTH, null=True)


class FormOptions(models.Model):
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    contact_options = models.ForeignKey(ContactOptions, on_delete=models.CASCADE)
    page_options = models.ForeignKey(PageOptions, on_delete=models.CASCADE)
