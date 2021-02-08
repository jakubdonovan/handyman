from django.contrib import admin

# Register your models here.
from .models import (
    ContactOptions,
    FormOptions,
    Image,
    PageOptions,
    Portfolio,
    ProfessionOption,
    Review,
)

admin.site.register(ContactOptions)
admin.site.register(PageOptions)
admin.site.register(Portfolio)
admin.site.register(ProfessionOption)
admin.site.register(Review)
admin.site.register(Image)


def full_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()


@admin.register(FormOptions)
class FormOptionAdmin(admin.ModelAdmin[FormOptions]):
    """Admin panel example for ``FormOption`` model."""

    list_display = (full_name,)
