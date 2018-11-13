from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def view_cart(request):
    """ a view that rdners the car contents page """
    return render(request, "cart.html")


@login_required
def add_to_cart(request, id):
    """ add a quantity of hte specified product to teh cart"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    # return redirect('feature_detail', id)
    return redirect('view_cart')


@login_required
def adjust_cart(request, id):
    """Adjust the quantity of hte specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
