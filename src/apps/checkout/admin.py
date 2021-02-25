from django.contrib import admin

# Register your models here.
from .models import ContactOptions, PageOptions, Stage

admin.site.register(PageOptions)
admin.site.register(Stage)


def full_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()


@admin.register(ContactOptions)
class ContactFormOptionAdmin(admin.ModelAdmin[ContactOptions]):
    """Admin panel example for ``ContactOption`` model."""

    list_display = (full_name,)
