from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from checkout.models import OrderLineItem, Order

# Create your views here.


def index(request):
    """Return index.html file"""
    return render(request, 'index.html')


@login_required
def logout(request):
    """log out user"""
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('index'))


def login(request):
    """log in user return login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        if user:
            auth.login(user=user, request=request)
            messages.success(request, "your're logged in")
            return redirect(reverse('index'))
        else:
            login_form.add_error(None, "UN or PW is wrong")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "you are regsitered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "not registered")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
                  {"registration_form": registration_form})


def get_order_lineitems(id):
    user_order_details = (OrderLineItem.objects.filter(
        order_id=id))
    return user_order_details


def user_profile(request):
    """prfole page"""
    user = User.objects.get(email=request.user.email)
    # orders
    user_orders = Order.objects.filter(
        buyer_id=user.id).order_by('-id')

    for orders in user_orders:
        user_order_details = get_order_lineitems(orders.id)
        # user_order_details = (OrderLineItem.objects.filter(
        #     order_id=orders.id))
        print(user_order_details)

    for o in user_orders:
        user_order_items = (OrderLineItem.objects.filter(
            order_id=o.id))

    return render(request, 'profile.html', {'profile': user,
                                            'user_orders': user_orders,
                                            'user_order_details': user_order_details,
                                            'user_order_items': user_order_items})


def get_order_details(request, pk):
    user_order_details = (OrderLineItem.objects.filter(
        order_id=pk))
    return render(request, 'orders.html', {'user_order_details': user_order_details})
