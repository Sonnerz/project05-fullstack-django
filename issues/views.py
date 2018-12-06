from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Bug, Feature, BugComment
from blog.models import PostComment
from .forms import BugForm, FeatureForm, BugCommentForm, AdminBugForm, AdminFeatureForm
from uuid import uuid4
from cart.views import add_to_cart
from checkout.models import OrderLineItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import BugsFilter, FeaturesFilter
from django.db.models import Q
from django.contrib import messages


# Create your views here.


@login_required
def get_all_bugs(request):
    """
    Create a view that will return a list
    of all Bugs that were published prior to 'now'
    and render them to the bugs.html template
    """
    # GET BUGS ORDER THEM BY PUBLISHED DATE
    bugs = Bug.objects.filter(published_date__lte=timezone.now
                              ()).order_by('-published_date')
    # GET STATUS CHOSEN BY USER FROM DROPDOWN
    statusvalue = request.GET.get('status', '')
    # FILTER THE BUGS QUERYSET BY STATUS VALUE SENT IN REQUEST
    bugs_filter = BugsFilter(request.GET, queryset=bugs)

    # PAGE THE BUGS FILTER QUERYSET - 4 BUGS PER PAGE
    paginator = Paginator(bugs_filter.qs, 4)
    page = request.GET.get('page', 1)

    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    # RETURN BUGS QUERYSET, FILTERED BUGS QUERYSET AND USER SELECTED STATUS VALUE
    return render(request, "bugs.html", {'bugs': bugs, 'filter': bugs_filter, 'statusvalue': statusvalue})


@login_required
def bug_detail(request, pk):
    """
    Create a view that returns a single Bug object based on the bug ID (pk) and
    render it to the bugdetail.html template or return a 404 error if bug is not found
    """
    # GET SPECIFIC BUGS BY ITS' ID
    bug = get_object_or_404(Bug, pk=pk)
    # INCREASE VIEW COUNT BY 1
    bug.views += 1
    bug.save()
    # GET COMMENTS ABOUT THIS BUG.
    # ONLY RETURN COMMENTS THAT HAVE NOT BEEN HIDDEN BY ADMIN
    bugcomments = BugComment.objects.filter(~Q(is_hidden=True),
                                            bug_id=pk).order_by('-created_date')

    # PAGE THE COMMENTS
    paginator = Paginator(bugcomments, 4)
    page = request.GET.get('page', 1)

    try:
        bugcomments = paginator.page(page)
    except PageNotAnInteger:
        bugcomments = paginator.page(1)
    except EmptyPage:
        bugcomments = paginator.page(paginator.num_pages)

    # COMMENT FORM - TEXTAREA TO CREATE COMMENT
    if request.method == "POST":
        form = BugCommentForm(request.POST)
        if form.is_valid():
            bugcomment = form.save(commit=False)
            # ADD CURRENT USER AS COMMENT AUTHOR
            bugcomment.author = request.user
            # ADD CURRENT BUG AS FOREIGN KEY FOR COMMENT
            bugcomment.bug = bug
            bugcomment.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugCommentForm()

    return render(request, "bugdetail.html", {'bug': bug, 'bugcomments': bugcomments, 'comment_form': form})


def create_ref():
    """
    Create custom reference number for Bugs using random letters and numbers
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
    # GET BUG BY ID (PK) FOR EDIT MODE
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        if "cancel" in request.POST:
            return redirect(bug_detail, bug.pk)
        # POPULATE FORM WITH BUG DETAILS IF EDIT MODE
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            # ADD CURRENT USER AS AUTHOR
            bug.author = request.user
            # ADD GENERATED CUSTOM REFERENCE
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
    # GET BUG BY ID (PK)
    bug = get_object_or_404(Bug, pk=pk)
    bug.votes += 1
    bug.save()

    return redirect(bug_detail, bug.pk)


@login_required
def get_all_features(request):
    """
    Create a view that will return a list
    of features that were published prior to 'now'
    and render them to the features.html template
    """
    # GET FEATURES WHERE STATUS IS NOT 'PENDING PAYMENT'
    features = Feature.objects.filter(
        ~Q(status='Pending Payment')).order_by('-published_date')

    # GET STATUS CHOSEN BY USER FROM DROPDOWN
    statusvalue = request.GET.get('status', '')
    # FILTER THE FEATURES QUERYSET BY STATUS VALUE SENT IN REQUEST
    features_filter = FeaturesFilter(request.GET, queryset=features)

    # PAGE THE QUERYSET - 4 FEATURES PER PAGE
    paginator = Paginator(features_filter.qs, 4)
    page = request.GET.get('page', 1)

    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    # RETURN FEATURES QUERYSET, FILTERED QUERYSET AND STATUS VALUE
    return render(request, "features.html", {'features': features, 'filter': features_filter, 'statusvalue': statusvalue})


@login_required
def feature_detail(request, pk):
    """
    Create a view that returns a single
    feature object based on the feature ID (pk) and
    render it to the featuredetail.html template
    or return a 404 error if feature is not found
    """
    # CHECK IF REFERRER IS ORDERS PAGE
    # SHOW 'BACK TO ORDERS' BUTTON IF ORDERS PAGE IS REFERRER
    from_orders = False
    refering_order = ""
    if "orders" in request.META.get('HTTP_REFERER'):
        from_orders = True
        refering_order = request.META.get('HTTP_REFERER')

    # GET FEATURE USING ID (PK)
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    # GET ALL ORDERS FOR THIS FEATURE FROM THE ORDERLINEITEM TABLE
    feature_orders = OrderLineItem.objects.filter(
        feature_id=pk).order_by('-id')
    # GET ORDER DETAILS FOR THIS FEATURE
    # declare and set vars - total_hrs_bought, number_of_times_ordered, total_cost_of_dev
    total_hrs_bought = 0
    number_of_times_ordered = 0
    total_cost_of_dev = feature.dev_hours_req * 50
    # GET ORDERS COUNT FOR THIS FEATURE AND TOTAL HOURS BOUGHT
    for orders in feature_orders:
        number_of_times_ordered += 1
        total_hrs_bought += orders.quantity
    # GET TOTAL MONEY RAISED FOR THIS FEATURE (50 IS COST PER HOUR)
    total_money_raised = total_hrs_bought * 50
    total_money_needed = total_cost_of_dev - total_money_raised
    total_hours_needed = feature.dev_hours_req - total_hrs_bought
    # CREATE DICTIONARY OF DATA TO RETURN TO PAGE FOR DISPLAYING
    totals = {'total_hrs_bought': total_hrs_bought,
              'total_money_raised': total_money_raised,
              'total_money_needed': total_money_needed,
              'number_of_times_ordered': number_of_times_ordered,
              'total_cost_of_dev': total_cost_of_dev,
              'total_hours_needed': total_hours_needed}
    return render(request, "featuredetail.html", {'feature': feature, 'feature_orders': feature_orders,
                                                  'totals': totals, 'from_orders': from_orders, 'refering_order': refering_order})


def create_feature_ref():
    """
    Create custom reference number for Features using random letters and numbers
    Feat-xxxxx
    """
    return str("Feat-")+str(uuid4())[:5]


@login_required
def new_feature(request):
    """
    Create a view that allows users to create a new feature
    """

    if request.method == "POST":
        # CANCEL BUTTON
        if "cancel" in request.POST:
            return redirect(get_all_features)
        form = FeatureForm(request.POST)
        if form.is_valid():
            # NEW FEATURE SAVED WITH STATUS: 'Pending Payment'
            feature = form.save(commit=False)
            feature.author = request.user
            feature.ref = create_feature_ref()
            feature.save()
            # GET THIS FEATURE ID BASED ON REF JUST CREATED - feature.ref = create_feature_ref()
            this_feature = Feature.objects.filter(ref=feature.ref)
            # ADD NUMBER OF HOURS TO CART (MINIMUM OF 2 FOR NEW FEATURE) FOR THIS FEATURE
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
    edit a feature depending if the Feature ID is null or not
    """

    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        # CANCEL BUTTON
        if "cancel" in request.POST:
            return redirect(feature_detail, feature.pk)
        # EDIT AND SAVE FEATURE DETAILS BASED ON ID (PK)
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.save()
            return redirect(feature_detail, feature.pk)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'featureform_edit.html', {'form': form})


@login_required
def bug_comment_report(request, pk):
    """
    Create a view that will allow a user to report
    a bug comment if inappropriate, etc.
    """
    # GET SPECIFIC COMMENT BY ID
    bugcomment = get_object_or_404(BugComment, pk=pk)
    # SET COMMENT FIELD 'IS_REPORTED' TO TRUE
    bugcomment.is_reported = True
    bugcomment.save()
    return redirect(bug_detail, bugcomment.bug.id)


@login_required
def super_admin(request):
    """
    Create a view that will return a list
    of reported comments for an admin to hide from users.
    """
    # GET COMMENTS IF 'IS_REPORTED' IS TRUE
    bugcomments = BugComment.objects.filter(
        is_reported=True).order_by('-created_date')

    return render(request, "superadmin.html", {'bugcomments': bugcomments})


@login_required
def comment_toggle_hide(request, pk):
    """
    Create a view that will hide a reported bug comment.
    """
    # GET THE REPORTED COMMENT BY ID
    reported_comment = get_object_or_404(BugComment, pk=pk)
    # TOGGLE COMMENT HIDDEN/SHOW
    reported_comment.is_hidden = not reported_comment.is_hidden
    if not reported_comment.is_hidden:
        reported_comment.is_reported = not reported_comment.is_reported
    reported_comment.save()

    return redirect(super_admin)


@login_required
def admin_edit(request, pk):
    """
    Create a view that will allow an admin
    to edit all details of an item (bug or feature)
    If it's a bug then 'b' passed in querystring
    If it's a feature then 'f' passed in querystring
    """
    # GET TYPE FROM QUERYSTRING - B OR F
    typeofitem = request.GET.get('type')
    # IF 'B' THEN IT'S A BUG
    if typeofitem == "b":
        bug = get_object_or_404(Bug, pk=pk)
        if request.method == "POST":
            if "cancel" in request.POST:
                return redirect(bug_detail, bug.pk)
            form = AdminBugForm(request.POST, request.FILES, instance=bug)
            if form.is_valid():
                bug = form.save(commit=False)
                bug.save()
                return redirect(bug_detail, bug.pk)
        else:
            form = AdminBugForm(instance=bug)
        return render(request, 'admin_edit.html', {'form': form})
    # ELSE IF 'F' THEN IT'S A FEATURE
    elif typeofitem == "f":
        feature = get_object_or_404(Feature, pk=pk)
        if request.method == "POST":
            if "cancel" in request.POST:
                return redirect(feature_detail, feature.pk)
            form = AdminFeatureForm(
                request.POST, request.FILES, instance=feature)
            if form.is_valid():
                feature = form.save(commit=False)
                feature.save()
                return redirect(feature_detail, feature.pk)
        else:
            form = AdminFeatureForm(instance=feature)
        return render(request, 'admin_edit.html', {'form': form})
    return redirect(get_all_features)
