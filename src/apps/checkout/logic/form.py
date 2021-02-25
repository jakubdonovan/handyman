from typing import Any, Text

from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from phonenumber_field.formfields import PhoneNumberField
from src.apps.checkout.models import PageOptions


# Create the form class.
class ContactForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        widget=TextInput(attrs={"placeholder": "John"}),
    )
    last_name = forms.CharField(
        label="Last Name", widget=TextInput(attrs={"placeholder": "Doe"})
    )

    phone_number = PhoneNumberField(
        region="GB",
        widget=(
            TextInput(
                attrs={
                    "class": "border-gray-200 w-full",
                    "placeholder": "07391205592",
                }
            )
        ),
    )
    whats_app = forms.CheckboxInput()

    def __init__(self, *args, **kwargs):
        super().__init__()

        visible_fields:Any = self.visible_fields()
        for visible in visible_fields:

            if not (field_class := visible.field.widget.attrs).get("class"):
                field_class[
                    "class"
                ] = "px-4 py-2 flex rounded-md border-gray-200"
            else:
                field_class["class"] += " px-4 py-2 flex rounded-md"

    # class Meta:
    #     model = ContactOptions
    #     fields = [
    #         "first_name",
    #         "last_name",
    #         "phone_number",
    #         "messenger",
    #         "whatsapp",
    #     ]


# Create the form class.
class PageOptionsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs[
                "class"
            ] = "px-4 py-2 flex rounded-md border-gray-200 gap-4"

    class Meta:
        model = PageOptions
        fields = [
            # "professions",
            "profile_image",
            # "review_name",
            # "review_quote",
            # "review_image",
            # "portfolio_image",
            # "portfolio_description",
        ]
