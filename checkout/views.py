from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

stripe.api_key = 'sk_test_51PIvxGATjyvbumToY65Fj2KhjXGbzwzPPcRlTfsmmfVHCtmjsiFKwgaVK1RrVdPpB1Uo0O685W2IsQcVvr7AuHny00WE3xd5ML'

def checkout(request):
    """
    A view to return the checkout page
    """
    # get bag from session + check if it's empty
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    # Create a PaymentIntent
    payment_intent = stripe.PaymentIntent.create(
        amount=stripe_total,  # amount in cents
        currency='usd',
    )

# create instance for order form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PIvxGATjyvbumTol8JLREvXxbVqfydItJDu7lGDAzsmlxG9an1kOuuKOCw30wTsTTjLarwb2iFLpgS0TliXv7fJ00RKcaEdtD',
        'client_secret': payment_intent.client_secret,
    }
# rendering it all out
    return render(request, template, context)
