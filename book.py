class Book:
    
    def __init__(self,name,liste_order=[]):
        self.name=name
        self.liste_order=liste_order
        
    def insert_buy (self,q,p, type_ordre="BUY"):
        ordre=Order(q,len(self.liste_order)+1,p,type_ordre)
        self.liste_order.append(ordre)
        self.affichage(ordre)
        
    
    def insert_sell(self,q,p, type_ordre="SELL"):
        ordre=Order(q,len(self.liste_order)+1,p,type_ordre)
        self.liste_order.append(ordre)
        self.affichage(ordre)
        
    def affichage(self,ordre):
        print("--- Insert " + str(ordre.type_ordre) + " "+str(ordre.quantite)+"@"+str(ordre.prix)+" id="+str(ordre.ID)+ " on "+self.name )
        print("\n")
        print("Book on "+self.name+"\n")
        
        for i in self.liste_order:
            print("           "+str(i.type_ordre)+" "+ str(i.quantite) +"@"+str(i.prix) + " id="+str(i.ID))
        print("\n")
        print("\n")
    
    def tri_ordre(self):
        liste=sorted(self.liste_order,key=lambda x: x.type_ordre)
    
    
class Order:
    nb_id = itertools.count(1)  

    def __init__(self, quantity, price, type):
        self.quantity = quantity
        self.price = price
        self.type = type.upper()
        self.id = next(self.nb_id)  

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def set_quantity(self, quantity):
        self.quantity = quantity
        
    def get_id(self):
        return self.id
    
    def __str__(self):  
        return self.type.upper() + " %s@%s id=%s" % (self.quantity, self.price, self.id)
    def __lt__(self, other):   
        return self.price <= other.price
    def __eq__(self, other):
        return ((self.quantity == other.quantity) and (self.price == other.price))
    


def main():
    book = Book("TEST")
    book.insert_buy(10, 10.0)
    book.insert_sell(120, 12.0)
    book.insert_buy(5, 10.0)
    book.insert_buy(2, 11.0)
    book.insert_sell(1, 10.0)
    book.insert_sell(10, 10.0)

if name == "main":
    main()
