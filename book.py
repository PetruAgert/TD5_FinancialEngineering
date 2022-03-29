class Deal:
    def __init__(self, quantity, price, book_name):
  
        self.quantity = quantity
        self.price = price
        self.book_name = book_name


    def get_price(self):
        return self.price
    
    def __str__(self):
        return 'Execute the deal of quantity {quantity} at {price} dollars on {book}'.format(quantity=self.quantity, price=self.price,book=self.book_name)
