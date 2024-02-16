from .cart import Cart

# create context processor
def cart(request):
    # return default data from our cart
    return {'cart':Cart(request)}