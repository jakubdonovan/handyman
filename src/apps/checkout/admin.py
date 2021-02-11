from django.contrib import admin

# Register your models here.
from .models import (
    CheckoutOptions,
    Portfolio,
    Profession,
    Review,
)

admin.site.register(Portfolio)
admin.site.register(Profession)
admin.site.register(Review)


def full_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()


@admin.register(CheckoutOptions)
class CheckoutFormOptionAdmin(admin.ModelAdmin[CheckoutOptions]):
    """Admin panel example for ``CheckoutOption`` model."""

    list_display = (full_name,)
