from dataclasses import dataclass

@dataclass
class Item:
    code : int
    name : str
    cents : int
    
    def unitprice(self):
        return self.cents / 100.0
    
    def price(self, quantity : int):
        return self.cents * quantity / 100.0
    
    def __str__(self):
        return f"{self.name} ({self.code}, {self.unitprice()}€)"

beer = Item(56273, "Zundert 33 cl", 250)
print(beer)
print(beer.unitprice())
print(beer.price(10))