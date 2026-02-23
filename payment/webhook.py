from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
import stripe
from decouple import config

stripe.api_key = config("STRIPE_SECRET_KEY")  # your test secret key
endpoint_secret = config("STRIPE_WEBHOOK_SECRET")  # from stripe listen

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout session completed event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        # Only mark paid orders that succeeded
        if session.get("payment_status") == "paid":
            try:
                order = Order.objects.get(id=session.get("client_reference_id"))
                order.paid = True
                order.stripe_id = session.get("payment_intent")
                order.save()
            except Order.DoesNotExist:
                return HttpResponse(status=404)

    # You can handle other event types here if needed
    return HttpResponse(status=200)