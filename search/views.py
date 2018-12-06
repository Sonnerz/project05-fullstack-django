from django.shortcuts import render
from django.db.models import Q
from issues.models import Bug, Feature
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def do_search(request):
    '''
    Search for Issues app.
    This function takes the user query and searches the Title, Ref and Tag fields
    Users can search for words or the bug/feature reference
    '''
    # FIELDS TO SEARCH
    lookup_fields = Q(title__icontains=request.GET['q']) | Q(
        ref__icontains=request.GET['q']) | Q(tag__icontains=request.GET['q'])
    # SEARCH FOR USER QUERY IN BUGS TITLE, REF OR TAG
    bugs = Bug.objects.filter(lookup_fields).distinct().order_by('-id')
    # SEARCH FOR USER QUERY IN FEATURES TITLE, REF OR TAG
    features = Feature.objects.filter(lookup_fields).distinct().order_by('-id')
    # SET GLOBAL VAR WITH USER SEARCH QUERY
    searchparam = request.GET['q']

    # PAGE THE BUGS QUERYSET
    paginator = Paginator(bugs, 6)
    page = request.GET.get('page', 1)

    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)

    # PAGE THE FEATURES QUERYSET
    paginator = Paginator(features, 6)
    page = request.GET.get('page', 1)

    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    # RETURN THE RESULTS AND SEARCH QUERY TO THE RESULTS PAGE
    return render(request, "results.html", {"bugs": bugs, "features": features, "q": searchparam})


@login_required
def do_search_ref(request):
    '''
    Search for REF ONLY.
    This function is only available on the search results page.
    Users can search for Bugs and Features by Ref only.
    '''
    # FIELD TO SEARCH - ref
    lookup_fields = Q(ref__icontains=request.GET['q'])
    # SEARCH BUGS REF FIELD
    bugs = Bug.objects.filter(lookup_fields).distinct()
    # SEARCH FEATURES REF FIELD
    features = Feature.objects.filter(lookup_fields).distinct()
    # SET GLOBAL VAR WITH USER SEARCH QUERY
    searchparam = request.GET['q']
    # RETURN THE RESULTS AND SEARCH QUERY TO THE RESULTS PAGE
    return render(request, "results.html", {"bugs": bugs, "features": features, "q": searchparam})


@login_required
def do_search_blog(request):
    '''
    Search for Blog app only.
    This function takes the user query and searches the Blog Title and Blog Tag fields only.
    '''
    # FIELDS TO SEARCH - TITLE AND TAG
    lookup_fields = Q(title__icontains=request.GET['b']) | Q(
        tag__icontains=request.GET['b'])
    # SEARCH POSTS
    posts = Post.objects.filter(lookup_fields).distinct()
    # SET GLOBAL VAR WITH USER SEARCH QUERY
    searchparam = request.GET['b']

    # PAGE THE BLOG POSTS QUERYSET
    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # RETURN THE RESULTS AND SEARCH QUERY TO THE RESULTS PAGE
    return render(request, "results_blog.html", {"posts": posts, "b": searchparam})
