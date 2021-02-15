from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from src.apps.checkout.models import ContactOptions, PageOptions
from phonenumber_field.formfields import PhoneNumberField


# Create the form class.
class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=TextInput())
    last_name = forms.CharField(label="First Name", widget=TextInput())

    phone_number = PhoneNumberField(region="GB")
    whats_app = forms.CheckboxInput()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for visible in self.visible_fields():

            if not (field_class := visible.field.widget.attrs).get("class"):
                field_class["class"] = "px-4 py-2 flex rounded-md border-gray-200 gap-4"
            else:
                field_class["class"] += " px-4 py-2 flex rounded-md gap-4"


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
            "professions",
            "profile_image",
            "review_name",
            "review_quote",
            "review_image",
            "portfolio_image",
            "portfolio_description",
        ]
