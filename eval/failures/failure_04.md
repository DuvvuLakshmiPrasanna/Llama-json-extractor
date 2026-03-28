# Failure 04 - eval_doc_14

## Source Document Text

```text
INVOICE
Vendor: Northwind Supplies
Invoice No: INV-0914
Date: 2025-02-17
Due Date: N/A
Currency: USD
Items:
- Wiring kit, qty 5, unit 50.00
- Clamp set, qty 4, unit 40.00
Subtotal: 410.00
Tax: 32.80
Total: 442.80
```

## Expected JSON

```json
{
  "vendor": "Northwind Supplies",
  "invoice_number": "INV-0914",
  "date": "2025-02-17",
  "due_date": null,
  "currency": "USD",
  "subtotal": 410.0,
  "tax": 32.8,
  "total": 442.8,
  "line_items": [
    { "description": "Wiring kit", "quantity": 5, "unit_price": 50.0 },
    { "description": "Clamp set", "quantity": 4, "unit_price": 40.0 }
  ]
}
```

## Model Output

```json
{
  "vendor": "Northwind Supplies",
  "invoice_number": "INV-0914",
  "date": "2025-02-17",
  "due_date": null,
  "currency": "USD",
  "subtotal": 410.0,
  "tax": 32.8,
  "total": 442.8
}
```

## What went wrong

Schema omission: required `line_items` key was missing.

## Why it likely failed

Some training examples include sparse OCR snippets with weak line item signals, causing occasional collapse to header-only extraction.

## Data-centric fix

Add at least 15 invoice examples where headers are noisy but line item blocks exist, and enforce that `line_items` is always present (empty array only when truly absent).
