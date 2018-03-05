class Cart():
    carts = {}

    def __init__(self):
        self.cartPrice = 0 # Total price of cart
        self.cartQty = 0 # Total item quantity of cart
        self.cart = {} # Item list

    def add_item(self, item):
        # If item exists increase quantity by 1 and price accordingly
        if item.id in self.cart:
            self.cart[item.id]['quantity'] += 1
            self.cart[item.id]['price'] += item.price
        # Else create a new entity in item list
        else:
            self.cart[item.id] = {'title': item.title, 'quantity': 1, 'price': item.price}
        # Increase cart's total price accordingly and increase total quantity by 1
        self.cartPrice += item.price
        self.cartQty += 1

    def delete_item(self, item):
        # Reduce cart's total price and quantity accordingly
        self.cartPrice -= self.cart[item.id]['price']
        self.cartQty -= self.cart[item.id]['quantity']
        # Delete entry
        del self.cart[item.id]
