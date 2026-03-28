# Failure 03 - eval_doc_11

## Source Document Text

```text
INVOICE
Vendor: Apex Steel Pvt Ltd
Invoice No: INV-0911
Date: 2025-02-15
Due Date: 2025-03-01
Currency: USD
Item: Angles, qty 10, unit 50.00
Subtotal: 500.00
Tax: 40.00
Total: 540.00
```

## Expected JSON

```json
{
  "vendor": "Apex Steel Pvt Ltd",
  "invoice_number": "INV-0911",
  "date": "2025-02-15",
  "due_date": "2025-03-01",
  "currency": "USD",
  "subtotal": 500.0,
  "tax": 40.0,
  "total": 540.0,
  "line_items": [
    { "description": "Angles", "quantity": 10, "unit_price": 50.0 }
  ]
}
```

## Model Output

```json
{
  "vendor": "Apex Steel Pvt Ltd",
  "invoice_number": "INV-0911",
  "date": "2025-02-15",
  "due_date": "2025-03-01",
  "currency": "USD",
  "subtotal": 500.0,
  "tax": 35.0,
  "total": 535.0,
  "line_items": [
    { "description": "Angles", "quantity": 10, "unit_price": 50.0 }
  ]
}
```

## What went wrong

Semantic value error: tax and total are numerically incorrect, though formatting and keys are valid.

## Why it likely failed

The model learned heuristic tax patterns from mixed-rate examples (5%, 8%, 10%) and overgeneralized instead of copying exact source values.

## Data-centric fix

Increase examples where tax must be copied exactly from text, including mixed locales and non-standard percentages; label with explicit `tax` and `total` values to discourage recomputation.
