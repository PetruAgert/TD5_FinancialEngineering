import pandas as pd

import itertools


class Intermediaire:
    def __init__(self, quantity, price, book_name):
  
        self.quantity = quantity
        self.price = price
        self.book_name = book_name

    
    def __str__(self):
        return 'Execute the deal of quantity {quantity} at {price} dollars on {book}'.format(quantity=self.quantity, price=self.price,book=self.book_name)

class Order:
    nb_of_id = itertools.count(1)  

    def __init__(self, quantity, price, type_of_order):
  
        self.quantity = quantity
        self.price = price
        self.type = type_of_order.upper()
        self.id = next(self.nb_of_id)  


    def __str__(self):  
        return self.type.upper() + " %s@%s id=%s" % (self.quantity, self.price, self.id)
    def __lt__(self, other):
        
        return self.price <= other.price



    def __eq__(self, other):

        return (self.quantity, self.price) == (other.quantity, other.price)
    def set_qty(self, newq):
        self.quantity = newq

class Book:
    def __init__(self, name='Default order book', buy_orders=[], sell_orders=[], execute_deals=[]):

        
        self.name = name
        self.buy_orders = buy_orders
        self.sell_orders = sell_orders
        self.execute_deals = execute_deals

    def insert_sell(self, quantity, price):
        
        
        sell_order = Order(quantity, price, type_of_order='sell')

        while len(self.buy_orders) != 0 and self.buy_orders[
            0].price >= sell_order.price and sell_order.quantity > 0:

            
            if sell_order.quantity > self.buy_orders[0].quantity:
                deal = Intermediaire(self.buy_orders[0].quantity, self.buy_orders[0].price, self.name)
                self.execute_deals.append(deal)

                new_qty = sell_order.quantity - self.buy_orders[0].quantity

                self.buy_orders.remove(self.buy_orders[0])

                sell_order.set_qty(new_qty)
                print(deal.__str__())

            
            else:
                deal = Intermediaire(sell_order.quantity, self.buy_orders[0].price, self.name)
                self.execute_deals.append(deal)

                
                self.buy_orders[0].set_qty(self.buy_orders[0].quantity - sell_order.quantity)

                sell_order.set_qty(0)

                if self.buy_orders[0].quantity == 0:
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
            0].price <= buy_order.price and buy_order.quantity > 0:

            
            if buy_order.quantity > self.sell_orders[0].quantity:
                deal = Intermediaire(self.sell_orders[0].quantity, self.sell_orders[0].price, self.name)
                self.execute_deals.append(deal)

                new_qty = buy_order.quantity - self.sell_orders[0].quantity

                
                self.sell_orders.remove(self.sell_orders[0])

                buy_order.set_qty(new_qty)
                print(deal.__str__())

           
            else:
                deal = Intermediaire(buy_order.quantity, self.sell_orders[0].price, self.name)
                self.execute_deals.append(deal)
                self.sell_orders[0].set_qty(self.sell_orders[0].quantity - buy_order.quantity)
                buy_order.set_qty(0)

                self._buy_orders.remove(self._buy_orders[0])

                if self.sell_orders[0].quantity == 0:
                    self.sell_orders.remove(self.sell_orders[0])

                print(deal.__str__())

        print(self.get_status())

        return None

    def insert_deals(self, deal):
     
        self._execute_deals.append(deal)
        return None

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
