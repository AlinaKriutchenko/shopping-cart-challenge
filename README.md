# Shopping Cart — Pricing Rules Challenge

A shopping cart implementation with configurable discount rules, built as a coding challenge.

The design uses the Strategy pattern — pricing rules are injected into the checkout at construction, making it easy to add or swap rules without changing core logic.

## Pricing rules implemented
- **Three-for-two** — buy 3, pay for 2
- **Bulk discount** — reduced price when buying above a quantity threshold
- **Free bundle** — a secondary item added free with a qualifying purchase

## Structure
```
src/
  checkout.py        # Checkout and scan logic
  product.py         # Product model
  pricing_rules/
    base_rule.py     # Abstract base class
    three_for_two.py
    bulk_discount.py
    free_vga_bundle.py
tests/               # unittest suite
```

## Run tests
```bash
python -m unittest discover tests
```

## Tech
- Python, unittest
