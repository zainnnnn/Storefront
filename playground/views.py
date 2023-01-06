
# from django.db.models import Q, Value, F, Func, Count, Max, Sum, Min, Avg, ExpressionWrapper, DecimalField
# from django.db.models.functions import Concat
# from store.models import Order, Product, Customer, Collection, OrderItem


# def say_hello(request):
#     # query_set = Product.objects.all()[:5]
#     # product = Product.objects.get(pk=1)
#     # product = Product.objects.filter(pk=0).exists()
#     # query_set = Product.objects.filter(unit_price__range=(1, 20))
#     # query_set = Product.objects.filter(title__icontains='coffee')
#     # query_set = Product.objects.filter(last_update__year=2021)
#     # query_set = Product.objects.filter(collection_id=1)
#     # query_set = Customer.objects.filter(email__endswith = '.com')
#     # query_set = Product.objects.filter(inventory__lt=10)
#     # query_set = Order.objects.filter(customer__id=1)
#     # query_set = Collection.objects.filter(featured_product__isnull=True)
#     # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
#     # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)#implement AND operator
#     # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(
#     #     unit_price__lt=20))  # implement OR operator
#     # query_set = Product.objects.filter(collection__id=1).order_by('-unit_price')
#     # query_set = Product.objects.order_by('unit_price')[0]``
#     # query_set = Product.objects.latest('unit_price')
#     # query_set = Product.objects.filter(id__in=OrderItem.objects.values(
#     #     'product_id').distinct()).order_by('title')

#     # query_set = Order.objects.select_related(
#     #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

#     # result = Product.objects.filter(collection_id=3).aggregate(
#     #     max=Max('unit_price'), min=Min('unit_price'), avg=Avg('unit_price'))

#     # query_set = Customer.objects.annotate(is_new=1 + F('id'))
#     # query_set = Customer.objects.annotate(
#     #     full_name=Func(F('first_name'), Value(
#     #         " "), F('last_name'), function='CONCAT')
#     # )
#     # query_set = Customer.objects.annotate(
#     #     full_name=Concat(('first_name'), Value(" "), ('last_name'))
#     # )
#     # discount = ExpressionWrapper(
#     #     F('unit_price') * 0.8, output_field=DecimalField())
#     # query_set = Product.objects.annotate(
#     #     discounted_price=discount
#     # )

#     # query_set = Customer.objects.annotate(
#     #     order_count=Count('order')
#     # ).filter(order_count__gt=5)

#     # query_set = Customer.objects.annotate(
#     #     total_spent=Sum(
#     #         F('order__orderitem__unit_price') * F('order__orderitem__quantity')
#     #     )
#     # )

#     query_set = Product.objects.annotate(
#         total_sales=Sum(
#             F('orderitem__unit_price') * F('orderitem__quantity')
#         )).order_by('-total_sales')[:5]
#     return render(request, 'hello.html', {'name': 'Zain', 'query_set': query_set})


from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem
from django.db import transaction


# def say_hello(request):
#     query_set = TaggedItem.objects.get_tags_for(Product, 1)
#     return render(request, 'hello.html', {'name': 'Zain', 'tags': list(query_set)})

# create/insert new row
# to update first read the record and then update it
# def say_hello(request):
#     # collection = Collection.objects.get(pk=11)
#     # collection.featured_product = None
#     # collection.save()
#     collection = Collection.objects.filter(pk=11).update(featured_product=None)
#     return render(request, 'hello.html', {'name': 'Zain'})


# using transactions for atomicity
def say_hello(request):
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()

    return render(request, 'hello.html', {'name': 'Zain'})
