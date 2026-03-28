# Purchase Order JSON Schema

This schema is binding for every purchase-order example in training and evaluation.

## Required object shape

```json
{
  "buyer": "string",
  "supplier": "string",
  "po_number": "string",
  "date": "YYYY-MM-DD",
  "delivery_date": "YYYY-MM-DD or null",
  "currency": "ISO-4217 3-letter code",
  "total": 0.0,
  "items": [
    {
      "item_name": "string",
      "quantity": 0,
      "unit_price": 0.0
    }
  ]
}
```

## Field rules

- `buyer` (string): Purchasing organization name exactly as shown in the PO; use empty string if absent.
- `supplier` (string): Vendor/supplier name exactly as shown; use empty string if absent.
- `po_number` (string): Purchase order identifier; use empty string when missing.
- `date` (string, `YYYY-MM-DD`): PO creation date normalized to ISO format; use empty string if date is ambiguous or absent.
- `delivery_date` (string or `null`): Requested/committed delivery date in ISO format if present; otherwise `null`.
- `currency` (string): ISO 3-letter code; empty string when unknown.
- `total` (float): PO total value as numeric float; keep numeric type even when source includes separators/commas.
- `items` (array): Array of line objects; use empty array when line entries are not present.

## Item object rules

- `item_name` (string): Material/service name for each ordered line.
- `quantity` (integer): Ordered quantity as integer.
- `unit_price` (float): Unit cost per line as float.

## Consistency decisions

- `delivery_date` is the only optional date field and must be `null` when missing.
- All required keys are always present.
- Missing text values use empty string; missing optional date uses `null`.
- Numeric values remain numeric (never quoted).
- No extra keys are included in purchase-order outputs.
