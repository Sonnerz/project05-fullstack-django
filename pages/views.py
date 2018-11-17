from django.shortcuts import render

# Create your views here.


def index(request):
    """ a view that displays an index page """
    return render(request, "index.html")


def info(request):
    """ a view that displays an info page """
    return render(request, "info.html")
