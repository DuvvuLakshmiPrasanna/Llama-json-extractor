# Baseline Responses (Base Llama 3.2)

Prompt used for all baseline runs:

Extract fields as JSON for invoice or purchase order. Return machine-readable JSON.

## eval_doc_01

````text
```json
{"vendor":"Apex Steel Pvt Ltd","invoice_number":"INV-0901"}
````

````

## eval_doc_02
```text
Here is the extracted information:
{"vendor":"Northwind Supplies","date":"2025-02-10","total":"424.20"}
````

## eval_doc_03

```text
{"vendor":"BlueRiver Logistics","invoice_number":"INV-0903","date":"2025-02-11","due_date":null,"currency":"USD","subtotal":390.0,"tax":31.2,"total":421.2,"line_items":[{"description":"Packing tape","quantity":10,"unit_price":9.0},{"description":"Cartons","quantity":15,"unit_price":20.0}]}
```

## eval_doc_04

```text
{"buyer":"Zenith Retail Ltd","supplier":"Orion Industrial","poNumber":"PO-7781","date":"2025/02/11","total":1220.0}
```

## eval_doc_05

```text
{"buyer":"Metro Hospital Group","supplier":"Crescent Pharma","po_number":"PO-7782","date":"2025-02-12","delivery_date":null,"currency":"EUR","total":880.0,"items":[{"item_name":"Syringes","quantity":40,"unit_price":12.0},{"item_name":"Gloves","quantity":20,"unit_price":20.0}]}
```

## eval_doc_06

```text
{"vendor":"GreenField Agro","invoice_no":"INV-0906","date":"2025-02-13","total":301.0,"currency":"USD"}
```

## eval_doc_07

```text
{"vendor":"UrbanGrid Energy","invoice_number":"INV-0907","date":"2025-02-14",}
```

## eval_doc_08

```text
{"vendor":"Summit Office Mart","invoice_number":"INV-0908","date":"2025-02-14","due_date":"2025-02-28","currency":"GBP","subtotal":250.0,"tax":20.0,"total":270.0,"line_items":[{"description":"Printer Ink","quantity":5,"unit_price":50.0}]}
```

## eval_doc_09

```text
The invoice appears to be from Velox Components and total is around 199.
```

## eval_doc_10

```text
{"buyer":"Helios Manufacturing","supplier":"Northwind Supplies","po_number":"PO-7786","date":"2025-02-15","delivery_date":"2025-02-22","currency":"USD","total":1540.0,"items":[{"item_name":"Motor","quantity":7,"unit_price":220.0}]}
```

## eval_doc_11

```text
{"vendor":"Apex Steel Pvt Ltd","invoice_number":"INV-0911","date":"15-02-2025","due_date":"01-03-2025","currency":"USD","subtotal":500,"tax":40,"total":540,"line_items":[{"description":"Angles","quantity":10,"unit_price":50}]}
```

## eval_doc_12

```text
{"vendor":"MedSure Devices","invoice_number":"INV-0912","date":"2025-02-16","due_date":null,"currency":"INR","subtotal":7000.0,"tax":null,"total":7000.0,"line_items":[{"description":"Sensor pack","quantity":2,"unit_price":3500.0}]}
```

## eval_doc_13

```text
{"buyer":"Atlas Warehousing","supplier":"Velox Components","po_num":"PO-7789","date":"2025-02-16","delivery_date":"2025-02-25","currency":"USD","total":990.0,"items":[{"item_name":"Crate","quantity":30,"unit_price":33.0}]}
```

## eval_doc_14

```text
{"vendor":"Northwind Supplies","invoice_number":"INV-0914","date":"2025-02-17","due_date":null,"currency":"USD","subtotal":"410.0","tax":"32.8","total":"442.8","line_items":[]}
```

## eval_doc_15

```text
Result: {vendor: "BlueRiver Logistics", total: 610.3}
```

## eval_doc_16

```text
{"buyer":"Pioneer Foods","supplier":"Orion Industrial","po_number":"PO-7792","date":"2025-02-18","delivery_date":null,"currency":"JPY","total":120000.0,"items":[{"item_name":"Conveyor Belt","quantity":2,"unit_price":60000.0}]}
```

## eval_doc_17

```text
{"vendor":"Crescent Pharma","invoice_number":"INV-0917","date":"2025-02-18","currency":"USD","subtotal":333.0,"tax":26.64,"total":359.64}
```

## eval_doc_18

```text
{"vendor":"Orion Industrial","invoice_number":"INV-0918","date":"2025-02-19","due_date":"2025-03-03","currency":"USD","subtotal":900.0,"tax":72.0,"total":972.0,"line_items":[{"description":"Panel set","quantity":9,"unit_price":100.0}]}
```

## eval_doc_19

```text
{"buyer":"NovaCare Clinics","supplier":"MedSure Devices","po_number":"PO-7795","date":"2025-02-19","currency":"USD","total":640.0}
```

## eval_doc_20

```text
Sure, I can help with that. The PO contains buyer Trinity Exports, supplier GreenField Agro, total 1110 USD.
```
