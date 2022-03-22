
class Order:
        def __init__(self, quantity, price, buy=True):
                self.__quantity = quantity
                self.price = price
                self.buy = buy
        def quantity(self):
                return self.__quantity if self.buy else -self.__quantity


class Book:
        def __init__(self,name):
                self.orders=[]
		self.name = name

        def insert_buy (self,quantity_order,price_order):
                order=Order(quantity_order,price_order,buy=True)
                self.orders.append(order)

	def insert_sell(self, quantity_order, price_order):
		order = Order(self, quantity_order, price_order, buy =False)
		self.orders.append(order)
