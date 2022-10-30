class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart (self):
        print("Added product to ",self.name,self.lastName,"Cart")

customer1 = Customer()
customer1.name = "Surachat"
customer1.lastName = "Loednaweporn"
customer1.addCart()
customer2 = Customer()
customer2.name = "Dark"
customer2.lastName = "Mhee"
customer2.addCart()
customer3 = Customer()
customer3.name = "Hajime"
customer3.lastName = "Fury"
customer3.addCart()
customer4 = Customer()
customer4.name = "Lycolis"
customer4.lastName = "Fury"
customer4.addCart()