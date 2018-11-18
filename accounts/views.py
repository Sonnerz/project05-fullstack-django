from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from checkout.models import OrderLineItem, Order
from django.http import HttpResponse
from issues.models import Bug, Feature
from issues.views import bug_detail
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.
@login_required
def acc_index(request):
    """Return acc_index.html page. Logged in home page"""
    # get user
    user = User.objects.get(email=request.user.email)
    # get 5 latest bugs submitted
    bugs = Bug.objects.filter(published_date__lte=timezone.now
                              ()).order_by('-published_date')[:5]
    # get 5 latest features requested
    features = Feature.objects.filter(published_date__lte=timezone.now
                                      ()).order_by('-published_date')[:5]
    return render(request, 'acc_index.html', {"bugs": bugs, 'features': features})


@login_required
def logout(request):
    """Log out user"""
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('index'))


def login(request):
    """Log in user and render login page"""
    if request.user.is_authenticated:
        return redirect(reverse('acc_index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        if user:
            auth.login(user=user, request=request)
            messages.success(request,  "You are logged in")
            return redirect(reverse('acc_index'))
        else:
            login_form.add_error(
                None, "The Username or Password is incorrect.")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """Render the user registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('acc_index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request, "You have been successfully registered.")
                return redirect(reverse('user_profile'))
            else:
                messages.error(
                    request, "Your registration attempt was unsuccessful.")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
                  {"registration_form": registration_form})


@login_required
def user_profile(request):
    """Profile page - shows users orders """
    user = User.objects.get(email=request.user.email)

    # get users' purchase orders
    user_orders = Order.objects.filter(
        buyer_id=user.id).order_by('-id')

    return render(request, 'profile.html', {'profile': user,
                                            'user_orders': user_orders})


@login_required
def get_order_details(request, pk):
    """Shows users order line items """
    # get the line items for each user order
    user_order_details = (OrderLineItem.objects.filter(
        order_id=pk))
    return render(request, 'orders.html', {'user_order_details': user_order_details, 'order_id': pk})


def validate_username(request):
    """
    View for ajax.
    Checks that username is unique as person completes registration form
    """
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def validate_email(request):
    """
    View for ajax.
    Checks that email exists in database for password reset
    """
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }

    if data['is_taken'] == False:
        data['error_message'] = 'That email is not registered.'
    return JsonResponse(data)
