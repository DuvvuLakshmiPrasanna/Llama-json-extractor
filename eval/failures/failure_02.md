# Failure 02 - eval_doc_07

## Source Document Text

```text
INVOICE
Vendor: UrbanGrid Energy
Invoice No: INV-0907
Date: 2025-02-14
Due Date: 2025-02-28
Currency: USD
Item: Meter parts, qty 4, unit 102.50
Subtotal: 410.00
Tax: 32.80
Total: 442.80
```

## Expected JSON

```json
{
  "vendor": "UrbanGrid Energy",
  "invoice_number": "INV-0907",
  "date": "2025-02-14",
  "due_date": "2025-02-28",
  "currency": "USD",
  "subtotal": 410.0,
  "tax": 32.8,
  "total": 442.8,
  "line_items": [
    { "description": "Meter parts", "quantity": 4, "unit_price": 102.5 }
  ]
}
```

## Model Output

```text
{"vendor":"UrbanGrid Energy","invoice_number":"INV-0907","date":"2025-02-14","due_date":"2025-02-28","currency":"USD","subtotal":410.0,"tax":32.8,"total":442.8,"line_items":[{"description":"Meter parts","quantity":4,"unit_price":102.5}],}
```

## What went wrong

Formatting failure: trailing comma before closing brace created invalid JSON.

## Why it likely failed

Training set underrepresents strict negative examples showing malformed commas as invalid; model still occasionally emits list-style punctuation patterns from pretraining.

## Data-centric fix

Add 12 difficult invoice examples with longer arrays and explicit gold outputs that end cleanly without trailing commas, plus counterexamples in data QA rejecting comma-final objects.
