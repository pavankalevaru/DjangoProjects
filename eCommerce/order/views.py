# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# from .models import OrderItem
# from .forms import OrderCreateForm
# from product.models import Cart


# def order_create(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item['product'],
#                     price=item['price'],
#                     quantity=item['quantity']
#                 )
#             cart.clear()
#         return render(request, 'product/created.html', {'order': order})
#     else:
#         form = OrderCreateForm()
#     return render(request, 'product/create.html', {'form': form})