class Order:
<<<<<<< HEAD
        def __init__(self, quantity, price,buy=True):
=======

	def __init__(self, quantity, price, buy=True):
		self.__quantity = quantity
		self.price = price
		self.buy = buy
	def quantity(self):
		return self.__quantity if self.buy else -self.__quantity


class Book:
	def __init__(self,name):
		self.name=name
		self.orders=[]
	def insert_buy (self,quantity_order,price_order):
		order=Order(quantity_order,price_order,buy=True)
		self.orders.append(order)

	def insert_sell(self,quantity_order,price_order):
		order=Order(self,quantity_order,price_order,buy=False)

        def __init__(self, quantity, price, buy=True):
>>>>>>> 9201fdf63549b2cdfba9973828e335d9df81ced4
                self.__quantity = quantity
                self.price = price
                self.type=type
        def quantity(self):
                return self.__quantity if self.buy else -self.__quantity


<<<<<<< HEAD
class Book:
<<<<<<< HEAD
        def __init__(self,name,orders=[]):
                self.orders=orders
                self.name = name

        def insert_buy (self,quantity,price):
                order=Order(quantity,price,True)
                self.orders.append(order)

        def insert_sell(self, quantity, price):
                order = Order(quantity, price,False)
                self.orders.append(order)
=======
        def __init__(self,name):
                self.orders=[]
                self.name = name

        def insert_buy (self,quantity_order,price_order):
                order=Order(self,quantity_order,price_order,True)
                self.orders.append(order)

        def insert_sell(self, quantity_order, price_order):
                order = Order(self, quantity_order, price_order, False)
                self.orders.append(order)
=======

>>>>>>> 2c1618037fc765b2461a5507a648061071906b42
>>>>>>> 9201fdf63549b2cdfba9973828e335d9df81ced4
