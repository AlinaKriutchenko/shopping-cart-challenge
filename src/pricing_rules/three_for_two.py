from typing import List
from product import Product
from pricing_rules.base_rule import PricingRule

class ThreeForTwo(PricingRule):
    def apply(self, items: List[Product]) -> float:
        atvs = [item for item in items if item.sku == 'atv']
        discount = (len(atvs) // 3) * atvs[0].price if atvs else 0.0
        return discount
