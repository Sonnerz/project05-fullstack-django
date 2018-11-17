from django.shortcuts import render
from django.db.models import Q
from issues.models import Bug, Feature
from blog.models import Post

# Create your views here.


def do_search(request):
    lookup_fields = Q(title__icontains=request.GET['q']) | Q(
        ref__icontains=request.GET['q'])
    bugs = Bug.objects.filter(lookup_fields).distinct()
    features = Feature.objects.filter(lookup_fields).distinct()
    searchparam = request.GET['q']
    return render(request, "results.html", {"bugs": bugs, "features": features, "q": searchparam})


def do_search_ref(request):
    lookup_fields = Q(ref__icontains=request.GET['q'])
    bugs = Bug.objects.filter(lookup_fields).distinct()
    features = Feature.objects.filter(lookup_fields).distinct()
    searchparam = request.GET['q']
    return render(request, "results.html", {"bugs": bugs, "features": features, "q": searchparam})


def do_search_blog(request):
    lookup_fields = Q(title__icontains=request.GET['b'])
    posts = Post.objects.filter(lookup_fields).distinct()
    searchparam = request.GET['b']
    return render(request, "results_blog.html", {"posts": posts, "b": searchparam})
