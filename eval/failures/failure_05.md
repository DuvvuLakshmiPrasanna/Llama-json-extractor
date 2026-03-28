# Failure 05 - eval_doc_19

## Source Document Text

```text
PURCHASE ORDER
Buyer: NovaCare Clinics
Supplier: MedSure Devices
PO Number: PO-7795
Date: 2025-02-19
Delivery Date: N/A
Currency: USD
Item: Diagnostic strips, qty 16, unit 40.00
Total: 640.00
```

## Expected JSON

```json
{
  "buyer": "NovaCare Clinics",
  "supplier": "MedSure Devices",
  "po_number": "PO-7795",
  "date": "2025-02-19",
  "delivery_date": null,
  "currency": "USD",
  "total": 640.0,
  "items": [
    { "item_name": "Diagnostic strips", "quantity": 16, "unit_price": 40.0 }
  ]
}
```

## Model Output

```json
{
  "buyer": "NovaCare Clinics",
  "supplier": "MedSure Devices",
  "po_number": "PO-7795",
  "date": "2025-02-19",
  "delivery_date": null,
  "currency": "USD",
  "total": "640.0",
  "items": [
    { "item_name": "Diagnostic strips", "quantity": 16, "unit_price": 40.0 }
  ]
}
```

## What went wrong

Type mismatch: `total` emitted as a string instead of float.

## Why it likely failed

A subset of training examples likely had serialized numerics in OCR text contexts that encouraged quoting of currency values.

## Data-centric fix

Add type-focused training examples and QA checks that reject any quoted numeric fields (`subtotal`, `tax`, `total`, `unit_price`) in output JSON.
