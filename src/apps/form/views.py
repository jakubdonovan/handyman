from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .logic.form import Form


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.
    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    context = {"form": Form}
    return render(request, "index.html", context)
