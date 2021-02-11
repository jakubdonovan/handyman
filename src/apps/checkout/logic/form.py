from django.forms import ModelForm
from src.apps.checkout.models import CheckoutOptions


# Create the form class.
class CheckoutForm(ModelForm):
    class Meta:
        model = CheckoutOptions
        fields = ["first_name", "last_name"]
