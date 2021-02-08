from django.forms import ModelForm
from django.forms.models import ModelFormOptions
from src.apps.form.models import FormOptions


# Create the form class.
class Form(ModelForm):
    class Meta:
        model = FormOptions
        fields: list[str] = ["first_name", "last_name"]
