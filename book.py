import pandas as pd

import itertools

class Deal:
    def __init__(self, quantity, price, book_name):
  
        self.quantity = quantity
        self.price = price
        self.book_name = book_name


    def get_price(self):
        return self.price
    
    def __str__(self):
        return 'Execute the deal of {quantity} at {price} on {book}'.format(quantity=self.quantity, price=self.price,book=self.book_name)

class Order:
    nb_of_id = itertools.count(1)  

    def __init__(self, quantity, price, type_of_order):
  
        self.quantity = quantity
        self.price = price
        self.type = type_of_order.upper()
        self.id = next(self.nb_of_id)  

    def get_qty(self):
        return self.quantity

    def get_price(self):
        return self.price

    def set_qty(self, quantity):
        self.quantity = quantity
        
    def get_id(self):
        return self.id
    
    def __str__(self):  
        return self.type.upper() + " %s@%s id=%s" % (self.quantity, self.price, self.id)
    def __lt__(self, other):
        
        return self.price <= other.price



    def __eq__(self, other):

        return (self.quantity, self.price) == (other.quantity, other.price)
 

class Book:
    def __init__(self, name='Default order book', buy_orders=[], sell_orders=[], execute_deals=[]):

        
        self.name = name
        self.buy_orders = buy_orders
        self.sell_orders = sell_orders
        self.execute_deals = execute_deals

    def insert_sell(self, quantity, price):
        
        
        sell_order = Order(quantity, price, type_of_order='sell')

        if quantity != 0:
            self.sell_orders.append(sell_order)
            self.sell_orders.sort()
            print('--- Insert {order} on {book}'.format(order=sell_order.__str__(), book=self.name))

        while len(self.buy_orders) != 0 and self.buy_orders[
            0].get_price() >= sell_order.get_price() and sell_order.get_qty() > 0:

            
            if sell_order.get_qty() > self.buy_orders[0].get_qty():
                deal = Deal(self.buy_orders[0].get_qty(), self.buy_orders[0].get_price(), self.name)
                self.execute_deals.append(deal)

                new_qty = sell_order.get_qty() - self.buy_orders[0].get_qty()

                # Fill the first buy order
                self.buy_orders.remove(self.buy_orders[0])

                sell_order.set_qty(new_qty)
                print(deal.__str__())

            
            else:
                deal = Deal(sell_order.get_qty(), self.buy_orders[0].get_price(), self.name)
                self.execute_deals.append(deal)

                
                self.buy_orders[0].set_qty(self.buy_orders[0].get_qty() - sell_order.get_qty())

                sell_order.set_qty(0)

                if self.buy_orders[0].get_qty() == 0:
                    self.buy_orders.remove(self.buy_orders[0])

                self.sell_orders.remove(self.sell_orders[0])

                print(deal.__str__())

        print(self.get_status())

        return None

    def insert_buy(self, quantity, price):
    
        
        buy_order = Order(quantity, price, type_of_order='buy')

        if quantity != 0:
            self.buy_orders.append(buy_order)
            self.buy_orders.sort()
            self.buy_orders.reverse()
            print('--- Insert {order} on {book}'.format(order=buy_order.__str__(), book=self.name))

        while len(self.sell_orders) != 0 and self.sell_orders[
            0].get_price() <= buy_order.get_price() and buy_order.get_qty() > 0:

            
            if buy_order.get_qty() > self.sell_orders[0].get_qty():
                deal = Deal(self.sell_orders[0].get_qty(), self.sell_orders[0].get_price(), self.name)
                self.execute_deals.append(deal)

                new_qty = buy_order.get_qty() - self.sell_orders[0].get_qty()

                
                self.sell_orders.remove(self.sell_orders[0])

                buy_order.set_qty(new_qty)
                print(deal.__str__())

           
            else:
                deal = Deal(buy_order.get_qty(), self.sell_orders[0].get_price(), self.name)
                self.execute_deals.append(deal)

                # Update of the new quantity
                self.sell_orders[0].set_qty(self.sell_orders[0].get_qty() - buy_order.get_qty())

                buy_order.set_qty(0)

                self._buy_orders.remove(self._buy_orders[0])

                if self.sell_orders[0].get_qty() == 0:
                    self.sell_orders.remove(self.sell_orders[0])

                print(deal.__str__())

        print(self.get_status())

        return None

    def insert_deals(self, deal):
     
        self._execute_deals.append(deal)
        return None

    def get_sell_order(self):
        return self._sell_orders

    def get_buy_orders(self):
        return self._buy_orders

    def get_status(self):
      
        
        status = ""

        status += 'Book on {}\n'.format(self.name.upper())
        order_book = self.create_df_order()
        status += order_book.to_string(index=False)
        status += '\n------------------------'
        return status

    def create_df_order(self):
       
        
        df_sell_orders = pd.DataFrame([sell_order.__dict__ for sell_order in self.sell_orders])
        df_buy_orders = pd.DataFrame([buy_order.__dict__ for buy_order in self.buy_orders])
        df_all_orders = df_sell_orders.append(df_buy_orders)
        df_all_orders.columns = ['QTY', 'PRICE', 'TYPE', 'ID']
        return df_all_orders
