from typing import List
from product import Product
from pricing_rules.base_rule import PricingRule

class Checkout:
    def __init__(self, pricing_rules: List[PricingRule] = None):
        self.items: List[Product] = []
        self.pricing_rules = pricing_rules if pricing_rules else []

    def scan(self, item: Product):
        self.items.append(item)

    def total(self) -> float:
        total = sum(item.price for item in self.items)
        for rule in self.pricing_rules:
            total -= rule.apply(self.items)
        return round(total, 2)

def scan_multiple(checkout: Checkout, item: Product, count: int):
    for _ in range(count):
        checkout.scan(item)
