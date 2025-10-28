from __future__ import annotations
from decimal import Decimal, getcontext
from typing import Iterable, List, Set, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: Decimal

def create_product(name: str, price: float | str | Decimal) -> Product:
    return Product(name, price=Decimal(str(price)))

def add_to_cart(cart: List[Product], product: Product) -> None:
    cart.append(product)

def track_unique_items(unique_items: Set[str], product: Product) -> None:
    unique_items.add(product.name)

def store_product(products_dict: Dict[str, Decimal], product: Product) -> None:
    products_dict[product.name] = product.price

def calculate_total(cart: Iterable[Product]) -> Decimal:
    return sum((p.price for p in cart), start=Decimal("0"))

# -----------------------------
# Bản tối ưu: xử lý một lượt
# -----------------------------
def summarize_cart(cart: Iterable[Product]) -> Tuple[Decimal, Set[str], Dict[str, Decimal]]:
    
    total = Decimal("0")
    unique_names: Set[str] = set()
    price_map: Dict[str, Decimal] = {}
    for p in cart:
        total += p.price
        unique_names.add(p.name)
        price_map[p.name] = p.price
    return total, unique_names, price_map

# -----------------------------
# Ví dụ dùng
# -----------------------------

cart: List[Product] = []
uniq: Set[str] = set()
prices: Dict[str, Decimal] = {}

p1 = create_product("  milk  ", 1.49)
p2 = create_product("Bread", "2.25")
p3 = create_product("milk", 1.49)

for p in (p1, p2, p3):
    add_to_cart(cart, p)
    track_unique_items(uniq, p)
    store_product(prices, p)

total = calculate_total(cart)
# Hoặc: total, uniq2, prices2 = summarize_cart(cart)

print(cart)     # [Product(...), ...]
print(uniq)     # {'Milk', 'Bread'}
print(prices)   # {'Milk': Decimal('1.49'), 'Bread': Decimal('2.25')}
print(total)    # Decimal('5.23')
