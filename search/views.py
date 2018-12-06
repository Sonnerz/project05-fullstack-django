from django.shortcuts import render
from django.db.models import Q
from issues.models import Bug, Feature
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def do_search(request):
    lookup_fields = Q(title__icontains=request.GET['q']) | Q(
        ref__icontains=request.GET['q']) | Q(tag__icontains=request.GET['q'])
    bugs = Bug.objects.filter(lookup_fields).distinct().order_by('-id')
    features = Feature.objects.filter(lookup_fields).distinct().order_by('-id')
    searchparam = request.GET['q']

    # Page the bugs queryset
    paginator = Paginator(bugs, 6)
    page = request.GET.get('page', 1)

    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)

    # Page the features queryset
    paginator = Paginator(features, 6)
    page = request.GET.get('page', 1)

    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)

    return render(request, "results.html", {"bugs": bugs, "features": features, "q": searchparam})


@login_required
def do_search_ref(request):
    lookup_fields = Q(ref__icontains=request.GET['q'])
    bugs = Bug.objects.filter(lookup_fields).distinct()
    features = Feature.objects.filter(lookup_fields).distinct()
    searchparam = request.GET['q']
    return render(request, "results.html", {"bugs": bugs, "features": features, "q": searchparam})


@login_required
def do_search_blog(request):
    lookup_fields = Q(title__icontains=request.GET['b']) | Q(
        tag__icontains=request.GET['b'])
    posts = Post.objects.filter(lookup_fields).distinct()
    searchparam = request.GET['b']

    # Page the blog posts queryset
    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "results_blog.html", {"posts": posts, "b": searchparam})
