class Cart():
    def __init__(self, request):
        self.session = request.session

        # get current session key if it exists
        cart = self.session.get('session_key')

        # if new user, create a new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # cart is available on all pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price )}
        
        self.session.modified = True
