from django.shortcuts import render, redirect
from .models import Cart
from orders.models import Order
from product.models import Product

# Create your views here.

#def cart_create(user=None):
#    cart_obj = Cart.objects.create(user = None)
#    print('new cart created')
#    return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html",{"cart":cart_obj})
    
    #print(request.session)
    #print(dir(request.session))
    #key = request.session.session_key
    #print(key)
    #request.session.set_expiry(300)
    #del request.session['cart_id']
    #request.session['cart_id']="12"
    #print(cart_id)
    #if cart_id is None:# and isinstance("card_id", int):
        #print('create new cart')
    #    cart_obj = cart_create()
    #    request.session['cart_id'] = cart_obj.id
    #    print("new cart created")
    #request.session['first_name'] = "Manish"
   # else:
        #print(cart_id)
        #try:
         #   cart_obj = Cart.objects.get(id=cart_id)
        #except Cart.DoesNotExist:
        #    user = None
    #request.session['user'] = request.user.username
    
def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:  
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            #print("Product is gone")
            return redirect("cart:home")
        cart_obj, new_cart = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
   #return redirect(product_obj.get_absolute_url())
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home") 

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        redirect("cart:home")
    else:
        order_obj = Order.objects.get_or_create(cart=cart_obj)
        print(order_obj[0])
    return render(request, "carts/checkout.html", {"object": order_obj[1]})