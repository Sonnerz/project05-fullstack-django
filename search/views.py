from django.shortcuts import render
from issues.models import Bug, Feature

# Create your views here.


def do_search(request):
    bugs = Bug.objects.filter(title__icontains=request.GET['q'])
    return render(request, "bugs.html", {"bugs": bugs})


def do_search_ref(request):
    bugs = Bug.objects.filter(ref__icontains=request.GET['q'])
    return render(request, "bugs.html", {"bugs": bugs})


def do_feat_search(request):
    features = Feature.objects.filter(title__icontains=request.GET['q'])
    return render(request, "features.html", {"features": features})


def do_feat_search_ref(request):
    features = Feature.objects.filter(ref__icontains=request.GET['q'])
    return render(request, "features.html", {"features": features})
