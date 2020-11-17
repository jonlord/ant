from django.http import HttpResponse
from .models import Order, Row
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


def index(request):
    return HttpResponse("You're at the orders index.")


@csrf_exempt
def place(request, client):
    order = request.POST['order']
    parse_order(order, client, 'Placed')

    return HttpResponse("Done", content_type="text/plain")


@csrf_exempt
def cancel(request, client):
    order = request.POST['order']
    parse_order(order, client, 'Deleted')

    return HttpResponse("Done", content_type="text/plain")


@csrf_exempt
def returns(request, client):
    order = request.POST['order']
    parse_order(order, client, 'Returned')

    return HttpResponse("Done", content_type="text/plain")


@csrf_exempt
def fulfill(request, client):
    order = request.POST['order']
    parse_order(order, client, 'Fulfilled')

    return HttpResponse("Done", content_type="text/plain")


def parse_order(order, client, status):
    order_dict = json.loads(order)

    print(order_dict['order_number'])
    print(client)

    date_obj = datetime.datetime.fromisoformat(order_dict['date'])

    order = Order(
        number=order_dict['order_number'],
        client=client.capitalize(),
        date=date_obj.date(),
        marketplace=order_dict['client'],
        eurozone=order_dict['items'][0].get('euro_zone', 0),
        status=status,
        read=False,
        processed=False
    )

    order.save()

    for item in order_dict['items']:
        row = Row(
            product_reference=item['product_reference'],
            color_reference=item['color_reference'],
            size_position=item['size'],
            quantity=item['quantity'],
            price=item['purchase_price'],
            order=order
        )

        row.save()

        print(item['product_reference'])
