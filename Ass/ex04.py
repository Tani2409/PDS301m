from dataclasses import dataclass


@dataclass
class GroceryItem:
    name: str
    category: str
    price: float
    stock: int

    def restock(self, amount: int):
        self.stock += amount
        print(f"Restocked {self.name}. New stock: {self.stock}")

    def sell(self, quantity: int):
        if quantity > self.stock:
            print(f"Not enough stock to sell {quantity} of {self.name}. Current stock: {self.stock}")
        self.stock -= quantity
        print(f"Sold {quantity} of {self.name}. Remaining stock: {self.stock}")

@dataclass
class Cart:
    def add_item(self, item: GroceryItem, quantity: int):
        if quantity > item.stock:
            print(f"Not enough stock to add {quantity} of {item.name} to cart. Current stock: {item.stock}")
            return
        item.sell(quantity)
        print(f"Added {quantity} of {item.name} to cart.")
        