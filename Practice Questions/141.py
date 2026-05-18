# 141: Create a class order which stores item and its price. 
# --> Use dunder function __gt__ to convey that:
#               order 1 > order 2 if price of order 1 > price of order 2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self,order2):
        return self.price > order2.price

order1= Order("Pen", 340)
order2 = Order("Book", 900)

print(order1 > order2)