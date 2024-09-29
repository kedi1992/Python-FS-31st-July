from django.shortcuts import render


def place_order(request):
    return render(request, 'place-order.html', {})


def make_payment(request):
    return render(request, 'make-payment.html', {})