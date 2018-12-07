from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def view_cart(request):
    """ A view that renders the cart contents """
    return render(request, "cart.html")


@login_required
def add_to_cart(request, id):
    """ Add a number of hours to the cart """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect('view_cart')


@login_required
def adjust_cart(request, id):
    """Adjust the quantity of the hours """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


@login_required
def remove_from_cart(request, id):
    """ Remove item from cart """
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect('view_cart')
