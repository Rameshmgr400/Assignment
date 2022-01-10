class Mobile:
    
    def show_model(model, price):
        model = model
        price = price
        print(f"Model: {model}")
        print(f"Price: {price}")
   
Iphone = Mobile()
Mobile.show_model("iPhone Xs Max", "89500")


class Mobile:
    brand = "Apple"
    price = "Rs. 980000"

    def name_price(self):
        print(f"The {self.brand} is {self.price}")

    def full_name(cls):
        return f"{cls.brand}"

    def iphone_price(cls):
        return f"{cls.price}"
    

iphone_Xsmax = Mobile()
iphone_Xsmax.name_price()
print(iphone_Xsmax.full_name())
print(iphone_Xsmax.iphone_price())

iphone_Xsmax.brand = "Samsung"
iphone_Xsmax.price = "Rs. 560000"
iphone_Xsmax.name_price()
print(iphone_Xsmax.full_name())
print(iphone_Xsmax.iphone_price())

Mobile.brand = "Xiaomi"
Mobile.price = "Rs. 39999"
iphone_Xsmax.name_price()
print(iphone_Xsmax.full_name())
print(iphone_Xsmax.iphone_price())