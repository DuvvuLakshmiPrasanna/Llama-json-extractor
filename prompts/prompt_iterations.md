# Prompt Iterations (Base Model Only)

## Document subset used

- eval_doc_01
- eval_doc_07
- eval_doc_15

## Prompt v1 (baseline)

Extract fields as JSON for invoice or purchase order. Return machine-readable JSON.

## Prompt v2 (strict formatting)

You are an information extraction engine.
Return ONLY one JSON object and nothing else.
Do not use markdown code fences.
Do not add explanations.
For invoice use keys: vendor, invoice_number, date, due_date, currency, subtotal, tax, total, line_items.
For purchase order use keys: buyer, supplier, po_number, date, delivery_date, currency, total, items.
Use null for missing optional values.

## Prompt v3 (schema + type constraints)

Task: Extract from the given document text.
Output requirements:

1. Output exactly one minified JSON object.
2. No prose, no markdown, no backticks.
3. Keep numeric fields as numbers, not strings.
4. Keep date fields in YYYY-MM-DD or null.
5. For invoice, line_items must be an array of objects with description, quantity, unit_price.
6. For purchase order, items must be an array of objects with item_name, quantity, unit_price.
   If unsure about missing optional fields, use null. If unsure about missing required text fields, use empty string.

## Prompt v4 (few-shot constrained)

You must extract structured JSON exactly following one of these patterns.

Example invoice output:
{"vendor":"Acme","invoice_number":"INV-1","date":"2025-01-01","due_date":null,"currency":"USD","subtotal":100.0,"tax":8.0,"total":108.0,"line_items":[{"description":"Widget","quantity":2,"unit_price":50.0}]}

Example PO output:
{"buyer":"BuyerCo","supplier":"SupplyCo","po_number":"PO-1","date":"2025-01-01","delivery_date":null,"currency":"USD","total":200.0,"items":[{"item_name":"Cable","quantity":10,"unit_price":20.0}]}

Now extract from the next document and return only JSON.
