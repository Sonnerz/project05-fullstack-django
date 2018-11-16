from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Bug, Feature, BugComment
from blog.models import PostComment
from .forms import BugForm, FeatureForm, BugCommentForm
from uuid import uuid4
from cart.views import add_to_cart
from checkout.models import OrderLineItem
from django.core.paginator import Paginator

# Create your views here.


@login_required
def get_all_bugs(request):
    """
    Create a view that will return a list
    of all Bugs that were published prior to 'now'
    and render them to the bugs.html template
    """
    bugs = Bug.objects.filter(published_date__lte=timezone.now
                              ()).order_by('-published_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 3)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)

    return render(request, "bugs.html", {'bugs': bugs})


@login_required
def bug_detail(request, pk):
    """
    Create a view that returns a single
    Bug object based on the bug ID (pk) and
    render it to the bugdetail.html template
    or return a 404 error if bug is not found
    """

    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    print("bug.views", bug.views)
    bugcomments = BugComment.objects.filter(
        bug_id=pk, created_date__lte=timezone.now()).order_by('-created_date')

    print("Bug Detail PK", pk)
    return render(request, "bugdetail.html", {'bug': bug, 'bugcomments': bugcomments})


@login_required
def bug_comment(request, pk):
    """
    Create a view that allows us to create
    a bug comment associated with a bug by id
    """
    bug = get_object_or_404(Bug, pk=pk)
    print("Bug Comment PK", pk)

    if request.method == "POST":
        if "cancel" in request.POST:
            return redirect(bug_detail, pk=pk)
        form = BugCommentForm(request.POST)
        if form.is_valid():
            bugcomment = form.save(commit=False)
            bugcomment.author = request.user
            bugcomment.bug = bug
            bugcomment.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugCommentForm()
    return render(request, "bugcommentform.html", {'bug': bug, 'comment_form': form})


def create_ref():
    """
    Create custom reference number for Bugs
    Bug-xxxxx
    """
    return str("Bug-")+str(uuid4())[:5]


@login_required
def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows us to create
    or edit a bug depending if the Bug ID
    is null or not
    """

    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        if "cancel" in request.POST:
            return redirect(get_all_bugs)
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.ref = create_ref()
            bug.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugform.html', {'form': form})


@login_required
def vote_bug(request, pk):
    """
    Vote up a bug
    """

    bug = get_object_or_404(Bug, pk=pk)
    print("Bug Vote PK", pk)
    bug.votes += 1
    bug.save()

    return render(request, "bugdetail.html", {'bug': bug})


@login_required
def get_all_features(request):
    """
    Create a view that will return a list
    of features that were published prior to 'now'
    and render them to the features.html template
    """
    features = Feature.objects.filter(published_date__lte=timezone.now
                                      ()).order_by('-published_date')

    return render(request, "features.html", {'features': features})


@login_required
def feature_detail(request, pk):
    """
    Create a view that returns a single
    feature object based on the feature ID (pk) and
    render it to the featuredetail.html template
    or return a 404 error if bug is not found
    """
    # Check if referer is orders page
    # Show back to orders button
    from_orders = False
    refering_order = ""
    if "orders" in request.META.get('HTTP_REFERER'):
        from_orders = True
        refering_order = request.META.get('HTTP_REFERER')

    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    # Get all orders for this Feature from the OrderLineItem table
    feature_orders = OrderLineItem.objects.filter(
        feature_id=pk).order_by('-id')
    # Get the total money raised for this Feature
    total_hrs_bought = 0
    number_of_times_ordered = 0
    for orders in feature_orders:
        number_of_times_ordered += 1
        total_hrs_bought += orders.quantity
    # Get total money raised for this Feature
    total_money_raised = total_hrs_bought * 50
    total_money_needed = 500 - total_money_raised
    totals = {'total_hrs_bought': total_hrs_bought,
              'total_money_raised': total_money_raised,
              'total_money_needed': total_money_needed,
              'number_of_times_ordered': number_of_times_ordered, }
    return render(request, "featuredetail.html", {'feature': feature, 'feature_orders': feature_orders,
                                                  'totals': totals, 'from_orders': from_orders, 'refering_order': refering_order})


def create_feature_ref():
    """
    Create custom reference number for Features
    Feat-xxxxx
    """
    return str("Feat-")+str(uuid4())[:5]


@login_required
def new_feature(request):
    """
    Create a view that allows us to create
    a feature
    """

    if request.method == "POST":
        if "cancel" in request.POST:
            return redirect(get_all_features)
        form = FeatureForm(request.POST)
        if form.is_valid():
            # New Feature saved with status: 'Pending Payment'
            feature = form.save(commit=False)
            feature.author = request.user
            feature.ref = create_feature_ref()
            feature.save()
            # add to cart
            # get this Feature id based on ref just created
            this_feature = Feature.objects.filter(ref=feature.ref)
            for item in this_feature:
                add_to_cart(request, item.id)
            return redirect(get_all_features)
    else:
        form = FeatureForm()
    return render(request, 'featureform_new.html', {'form': form})


@login_required
def edit_feature(request, pk=None):
    """
    Create a view that allows us to
    edit a feature depending if the Feature ID
    is null or not
    """

    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        if "cancel" in request.POST:
            return redirect(feature_detail, feature.pk)
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.save()
            return redirect(feature_detail, feature.pk)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'featureform_edit.html', {'form': form})


@login_required
def vote_feature(request, pk):
    """
    Vote up a feature
    """

    feature = get_object_or_404(Feature, pk=pk)
    print("feature Vote PK", pk)
    feature.votes += 1
    feature.save()

    return render(request, "featuredetail.html", {'feature': feature})


@login_required
def bug_comment_report(request, pk):
    """
    Create a view that will allow a user to report
    a bug comment if inappropriate, etc.
    """
    bugcomment = get_object_or_404(BugComment, pk=pk)
    bugcomment.is_reported = True
    bugcomment.save()
    return redirect(bug_detail, bugcomment.bug.id)


@login_required
def super_admin(request):
    """
    Create a view that will return a list
    of reported comments for superadmin
    to delete or alter.
    """
    bugcomments = BugComment.objects.filter(
        is_reported=True).order_by('-created_date')

    return render(request, "superadmin.html", {'bugcomments': bugcomments})


@login_required
def comment_toggle_hide(request, pk):
    """
    Create a view that will hide a reported bug comment by superadmin.
    """
    reported_comment = get_object_or_404(BugComment, pk=pk)
    reported_comment.is_hidden = not reported_comment.is_hidden
    if not reported_comment.is_hidden:
        reported_comment.is_reported = not reported_comment.is_reported
    reported_comment.save()

    return redirect(super_admin)
