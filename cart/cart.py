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