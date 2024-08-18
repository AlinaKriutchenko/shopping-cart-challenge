from typing import List
from product import Product
from pricing_rules.base_rule import PricingRule

class BulkDiscount(PricingRule):
    def apply(self, items: List[Product]) -> float:
        ipads = [item for item in items if item.sku == 'ipd']
        if len(ipads) > 4:
            discount = len(ipads) * (ipads[0].price - 499.99)
            return discount
        return 0.0
