from .logic.request import fetch_sections
from django.shortcuts import render

from src.apps.checkout.logic.form import ContactForm, PageOptionsForm
from django.shortcuts import render
from formtools.wizard.views import CookieWizardView

from .logic.form import PageOptionsForm, ContactForm
from .models import Stage

import inspect

FORMS = [("contact_form", ContactForm), ("customize_form", PageOptionsForm)]

TEMPLATES = {
    "contact_form": "checkout-contact.html",
    "customize_form": "checkout-customize.html"
}

class CheckoutWizard(CookieWizardView):

    # def post(self, request, **kwargs):
        
    #     print(request.body)

    #     print(inspect.getmembers(request))
    #     return super().post( request )
        
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]


    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)

        form_options = [
            {

                "header": "Enter your contact details",
                "sub_header": "The contact information will be visible to your customers."

            },
            {
                "header": "Customize Your Page",
                "sub_header": "Personalize your page to continue."
            }
        ]

        rest = {"stages": Stage.objects.all(), "sections": fetch_sections, 'form_options': form_options[self.steps.step0]}

        return context | rest

    def done(self, form_list, **kwargs):
        print("done")
        result = {
            "form_data": [form.cleaned_data for form in form_list],
        },

        print(result)
        return render(
            self.request,
            "success.html",
            result
        )
