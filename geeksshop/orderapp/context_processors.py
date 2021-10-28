from .models import Order


def status(request):
    status_list = []
    if request.user.is_authenticated:
        status_list = Order.ORDER_STATUS_CHOICES

    return {
        'status': status_list
    }