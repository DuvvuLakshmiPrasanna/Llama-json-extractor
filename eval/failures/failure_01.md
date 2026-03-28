# Failure 01 - eval_doc_04

## Source Document Text

```text
PURCHASE ORDER
Buyer: Zenith Retail Ltd
Supplier: Orion Industrial
PO Number: PO-7781
PO Date: 2025-02-11
Delivery Date: 2025-02-20
Currency: USD
Line: Hydraulic hose, qty 8, unit 140.00
Total: 1220.00
```

## Expected JSON

```json
{
  "buyer": "Zenith Retail Ltd",
  "supplier": "Orion Industrial",
  "po_number": "PO-7781",
  "date": "2025-02-11",
  "delivery_date": "2025-02-20",
  "currency": "USD",
  "total": 1220.0,
  "items": [
    { "item_name": "Hydraulic hose", "quantity": 8, "unit_price": 140.0 }
  ]
}
```

## Model Output

```json
{
  "buyer": "Zenith Retail Ltd",
  "supplier": "Orion Industrial",
  "po_number": "PO-7781",
  "date": "2025-02-11",
  "delivery_date": "2025-02-20",
  "currency": "USD",
  "total": 1120.0,
  "items": [
    { "item_name": "Hydraulic hose", "quantity": 8, "unit_price": 140.0 }
  ]
}
```

## What went wrong

Total value was under-extracted (`1120.0` instead of `1220.0`) while schema and structure remained correct.

## Why it likely failed

The training set has fewer examples where line-item arithmetic conflicts with OCR-like total values; model appears to trust inferred multiplication more than explicit printed total.

## Data-centric fix

Add 8-10 curated PO examples where `total` intentionally differs from naive item multiplication due to freight/rounding adjustments, while still keeping schema fixed.
