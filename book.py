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
