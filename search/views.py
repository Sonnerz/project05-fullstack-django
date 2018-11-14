from django.shortcuts import render
from django.db.models import Q
from issues.models import Bug, Feature
from blog.models import Post

# Create your views here.


# def do_search(request):
#     bugs = Bug.objects.filter(title__icontains=request.GET['q'])
#     return render(request, "bugs.html", {"bugs": bugs})

# def do_search_ref(request):
#     bugs = Bug.objects.filter(ref__icontains=request.GET['q'])
#     return render(request, "bugs.html", {"bugs": bugs})

# def do_search(request):
#     lookup_fields = Q(title__icontains=request.GET['q']) | Q(
#         ref__icontains=request.GET['q'])
#     bugs = Bug.objects.filter(lookup_fields).distinct()
#     return render(request, "results.html", {"bugs": bugs, "features": features})


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
    lookup_fields = Q(title__icontains=request.GET['q'])
    posts = Post.objects.filter(lookup_fields).distinct()
    bugs = Bug.objects.filter(lookup_fields).distinct()
    features = Feature.objects.filter(lookup_fields).distinct()
    searchparam = request.GET['q']
    return render(request, "results.html", {"bugs": bugs, "features": features, "posts": posts, "q": searchparam})
