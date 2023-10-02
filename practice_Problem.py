class Product:
    def __init__(self,pname) -> None:
        self.pname = pname
        self.products = []
    def add_product(self,pname,price):
        product = (pname,price)
        self.products.append(product)
        print("Product has added")
    def buy_product(self,pname,price):
        product_found = False
        for name,money in self.products:
            if name == pname:
                    product_found = True
                    if price < money:
                        print("Not enough Money")
                    else:
                        print("here is you change",abs(money-price))
                        self.products.pop()
                        break
        if not product_found:
                print("No product")

class Shop(Product):
    pass
obj = Shop('Monpura')
obj.add_product("mangsho",100)
obj.add_product("murgi",150)
obj.buy_product("murgi",250)
obj.buy_product("mangsho",805)
for i in obj.products:
    print(i)




                
        