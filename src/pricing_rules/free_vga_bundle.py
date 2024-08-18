from typing import List
from product import Product
from pricing_rules.base_rule import PricingRule

class FreeVGABundle(PricingRule):
    def apply(self, items: List[Product]) -> float:
        macbook_count = sum(1 for item in items if item.sku == 'mbp')
        vga_count = sum(1 for item in items if item.sku == 'vga')
        
        free_vgas = min(macbook_count, vga_count)
        
        if free_vgas > 0:
            discount = free_vgas * 30.00 
            return discount
        
        return 0.0
