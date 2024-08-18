from abc import ABC, abstractmethod
from typing import List
from product import Product

class PricingRule(ABC):
    @abstractmethod
    def apply(self, items: List[Product]) -> float:
        # applies pricing rule and adds discount
        pass
