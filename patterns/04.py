import copy

class OrderPrototype:
    def __init__(self):
        self.order_number = None
        self.products = []
        self.total_price = 0.0
    
    def clone(self):
        return copy.deepcopy(self)

class Order:
    def __init__(self, prototype):
        self.order_number = prototype.order_number
        self.products = prototype.products
        self.total_price = prototype.total_price