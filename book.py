class Order:
        def __init__(self, quantity, price,buy=True):
                self.__quantity = quantity
                self.price = price
                self.type=type
        def quantity(self):
                return self.__quantity if self.buy else -self.__quantity


class Book:
        def __init__(self,name,orders=[]):
                self.orders=orders
                self.name = name

        def insert_buy (self,quantity,price):
                order=Order(quantity,price,True)
                self.orders.append(order)

        def insert_sell(self, quantity, price):
                order = Order(quantity, price,False)
                self.orders.append(order)
