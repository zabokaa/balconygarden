from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    """
    A view to return the checkout page
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    # get bag from session + check if it's empty
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

     # Check if a PaymentIntent already exists in the session
    if 'payment_intent_id' in request.session:
        # Retrieve the existing PaymentIntent
        intent = stripe.PaymentIntent.retrieve(request.session['payment_intent_id'])
    else:
        # Create a new PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Store the ID of the PaymentIntent in the session
        request.session['payment_intent_id'] = intent.id


# create instance for order form
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
# rendering it all out
    return render(request, template, context)