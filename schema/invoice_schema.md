# Invoice JSON Schema

This schema is binding for every invoice example in training and evaluation.

## Required object shape

```json
{
  "vendor": "string",
  "invoice_number": "string",
  "date": "YYYY-MM-DD",
  "due_date": "YYYY-MM-DD or null",
  "currency": "ISO-4217 3-letter code",
  "subtotal": 0.0,
  "tax": 0.0,
  "total": 0.0,
  "line_items": [
    {
      "description": "string",
      "quantity": 0,
      "unit_price": 0.0
    }
  ]
}
```

## Field rules

- `vendor` (string): Legal supplier or merchant name exactly as present in the document; use an empty string when unreadable or absent, never omit the key.
- `invoice_number` (string): Unique invoice identifier from the document header/body; use an empty string when absent.
- `date` (string, `YYYY-MM-DD`): Invoice issue date normalized to ISO format; if an exact day is missing but month/year exist, use empty string rather than guessing.
- `due_date` (string or `null`): Payment due date in `YYYY-MM-DD` if explicitly present; use `null` when due date is absent.
- `currency` (string): Three-letter ISO code (`USD`, `EUR`, `GBP`, `INR`, `JPY`, etc.); when symbol-only and ambiguous, use empty string.
- `subtotal` (float): Pre-tax amount as numeric float; use `0.0` only when the document truly reports zero or subtotal is unavailable and cannot be derived.
- `tax` (float or `null`): Tax amount as float when present; use `null` when no tax field exists.
- `total` (float): Final payable amount as numeric float from the document; use `0.0` only if total is not recoverable.
- `line_items` (array): Array of one or more item objects; if no line detail exists, use an empty array `[]`.

## Line item object rules

- `description` (string): Item/service label as printed; use empty string when blank.
- `quantity` (integer): Whole-number quantity; for non-integer source values, round only if source explicitly implies units and keep consistency by integer casting.
- `unit_price` (float): Per-unit cost as float; use `0.0` if missing and not inferable.

## Consistency decisions

- Optional date-like fields use `null` when missing.
- Optional amount fields (`tax`) use `null` when missing.
- Mandatory string keys are always present and default to empty string when unavailable.
- Mandatory numeric keys are always present as numeric types (never quoted strings).
- No additional keys are allowed in invoice outputs.
