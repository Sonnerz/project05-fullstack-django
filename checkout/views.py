from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from issues.models import Feature
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += quantity * feature.cost_per_hour
                order_line_item = OrderLineItem(
                    order=order,
                    feature=feature,
                    quantity=quantity

                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "your card was declined")

            if customer.paid:
                messages.error(request, "you have successffully paid")
                # Change Feature status to 'Target not Reached' or 'Under Review' before session cleared
                for id, quantity in cart.items():
                    feature = get_object_or_404(Feature, pk=id)
                    feature_orders = OrderLineItem.objects.filter(
                        feature_id=feature.id)
                    total_hrs_bought = 0
                    for orders in feature_orders:
                        total_hrs_bought += orders.quantity
                        if total_hrs_bought >= 10:
                            feature.status = "Under Review"
                        else:
                            feature.status = "Target not Reached"
                    feature.save()
                request.session['cart'] = {}
                return redirect(reverse('get_all_features'))
            else:
                messages.error(request, "unagle to take payemet")
        else:
            print(payment_form.errors)
            messages.error(
                request, "we were unable to take a payment with that card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
