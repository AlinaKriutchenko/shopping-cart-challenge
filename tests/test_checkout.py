import unittest
from checkout import Checkout, scan_multiple
from product import Product
from pricing_rules.three_for_two import ThreeForTwo
from pricing_rules.bulk_discount import BulkDiscount
from pricing_rules.free_vga_bundle import FreeVGABundle

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.checkout = Checkout(pricing_rules=[ThreeForTwo(), BulkDiscount(), FreeVGABundle()])
        self.mbp = Product(sku='mbp', name='MacBook Pro', price=1399.99)
        self.vga = Product(sku='vga', name='VGA adapter', price=30.00)
        self.atv = Product(sku='atv', name='Apple TV', price=109.50)
        self.ipad = Product(sku='ipd', name='Super iPad', price=549.99)

    def test_add_single_item(self):
        self.checkout.scan(self.atv)
        self.assertEqual(self.checkout.total(), 109.50)

    def test_add_multiple_items_no_discount(self):
        self.checkout.scan(self.atv)
        self.checkout.scan(self.ipad)
        self.assertEqual(self.checkout.total(), 659.49)

    def test_three_for_two_discount(self):
        scan_multiple(self.checkout, self.atv, 3) 
        self.assertEqual(self.checkout.total(), 219.00)  

    def test_three_for_two_discount(self):
        scan_multiple(self.checkout, self.atv, 5) 
        self.assertEqual(self.checkout.total(), 438.00) # no discount for 4th and 5th

    def test_bulk_discount(self):
        scan_multiple(self.checkout, self.ipad, 5) 
        self.assertEqual(self.checkout.total(), 2499.95) 

    def test_free_vga_with_macbook(self):
        self.checkout.scan(self.mbp)
        self.checkout.scan(self.vga) 
        self.assertEqual(self.checkout.total(), 1399.99) 

    def test_free_vga_with_multiple_macbooks(self):
        scan_multiple(self.checkout, self.mbp, 2)
        scan_multiple(self.checkout, self.vga, 2)  
        self.assertEqual(self.checkout.total(), 2799.98)

    def test_free_vga_with_multiple_macbooks(self):
        scan_multiple(self.checkout, self.mbp, 2)
        scan_multiple(self.checkout, self.vga, 3)  
        self.assertEqual(self.checkout.total(), 2829.98) # 3rd vga is not free   

if __name__ == '__main__':
    unittest.main()
