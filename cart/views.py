from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# summary
def cart_summary(request):
    # get cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    context = {
        'cart_products': cart_products,
        'quantities': quantities,
    }
    return render(request, "cart/cart_summary.html", context)

# add
def cart_add(request):
    # fetch cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # fetch data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)

        # save session 
        cart.add(product=product, cart_quantity=product_qty)

        # get cart quantity
        cart_quantity = cart.__len__()

        response = JsonResponse({'quantity: ': cart_quantity}) 
        # response = JsonResponse({'Product name: ': product.name})        
        return response

# delete
def cart_delete(request):
    context = {
        
    }
    return render(request, "cart/cart_delete.html", context)

# update
def cart_update(request):
    context = {
        
    }
    return render(request, "cart/cart_update.html", context)