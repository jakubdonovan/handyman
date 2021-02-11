from django.http.response import HttpResponseRedirect
from .logic.request import fetch_sections
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .logic.form import CheckoutForm


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.
    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """

    # Process Form Data
    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/success/")

    context = {"form": CheckoutForm, "sections": fetch_sections()}
    return render(request, "index.html", context)
