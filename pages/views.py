from django.shortcuts import render

# Create your views here.


def index(request):
    """ a view that displays an index page """
    return render(request, "index.html")


def about(request):
    """ a view that displays an about page """
    return render(request, "about.html")
