from transformers import pipeline
import gradio as gr
import json
import os
import re

# Use a lighter default model for low-memory hosting environments.
requested_model_id = os.getenv("MODEL_ID", "google/flan-t5-small")
fallback_model_ids = [
    requested_model_id,
    "google/flan-t5-base",
    "google/flan-t5-small",
]

pipe = None
loaded_model_id = None
loaded_task = None
last_error = None

for candidate in fallback_model_ids:
    print(f"Loading model: {candidate}")

    # Try explicit tasks first, then fallback to automatic task inference.
    pipeline_attempts = [
        ("text2text-generation", {"model": candidate, "device_map": "auto"}),
        ("text-generation", {"model": candidate, "device_map": "auto"}),
        (None, {"model": candidate, "device_map": "auto"}),
    ]

    for task_name, kwargs in pipeline_attempts:
        try:
            if task_name is None:
                pipe = pipeline(**kwargs)
                loaded_task = "auto"
            else:
                pipe = pipeline(task_name, **kwargs)
                loaded_task = task_name

            loaded_model_id = candidate
            break
        except Exception as err:
            last_error = err
            attempt_name = task_name or "auto"
            print(f"Pipeline init failed for model={candidate}, task={attempt_name}: {err}")

    if pipe is not None:
        break

if pipe is None:
    raise RuntimeError(
        "Unable to load any supported model. "
        f"Last error: {last_error}"
    )

print(f"Model loaded successfully: {loaded_model_id} (task={loaded_task})")


def _rule_based_extract(text):
    """
    Fallback parser for common invoice patterns when model output is not valid JSON.
    """
    data = {}

    invoice_match = re.search(r"invoice\s*#?\s*([A-Za-z0-9\-_/]+)", text, re.IGNORECASE)
    vendor_match = re.search(r"(?:from|vendor)\s*:\s*(.+)", text, re.IGNORECASE)
    date_match = re.search(r"(?:date|invoice\s+date)\s*:\s*([^\n]+)", text, re.IGNORECASE)
    due_match = re.search(r"due\s*:\s*([^\n]+)", text, re.IGNORECASE)
    items_match = re.search(r"items?\s*:\s*([^\n]+)", text, re.IGNORECASE)

    total_match = re.search(
        r"(?:total|amount)\s*:\s*([A-Za-z$€£]*\s?[0-9][0-9,]*(?:\.[0-9]{1,2})?\s?[A-Za-z]*)",
        text,
        re.IGNORECASE,
    )

    if invoice_match:
        data["invoice_number"] = invoice_match.group(1).strip()
    if vendor_match:
        data["vendor"] = vendor_match.group(1).strip()
    if date_match:
        data["date"] = date_match.group(1).strip()
    if due_match:
        data["due_date"] = due_match.group(1).strip()
    if items_match:
        data["items"] = [item.strip() for item in items_match.group(1).split(",") if item.strip()]
    if total_match:
        data["total_amount"] = total_match.group(1).strip()

    if data:
        data["extraction_mode"] = "rule_based_fallback"

    return data


# 🔹 Prediction function
def extract_json(text):
    """
    Extract structured invoice data from unstructured text.
    Converts raw invoice text to valid JSON format.
    """
    
    prompt = f"""Extract invoice data and return ONLY valid JSON. Do not include explanation, markdown, or extra text.

Use this JSON structure exactly (include keys even if null):
{{
  "invoice_number": null,
  "vendor": null,
  "date": null,
  "due_date": null,
  "total_amount": null,
  "items": []
}}

Invoice text:
{text}

Return valid JSON only:"""

    outputs = pipe(
        prompt,
        max_new_tokens=220,
        do_sample=False,
    )

    result = outputs[0]["generated_text"]

    # 🔹 Try to clean and parse JSON
    try:
        json_start = result.find("{")
        json_end = result.rfind("}") + 1
        
        if json_start == -1 or json_end == 0:
            fallback = _rule_based_extract(text)
            if fallback:
                return json.dumps(fallback, indent=2)
            return "⚠️ No JSON found in response:\n\n" + result
        
        json_str = result[json_start:json_end]
        parsed = json.loads(json_str)
        return json.dumps(parsed, indent=2)
    
    except json.JSONDecodeError as e:
        fallback = _rule_based_extract(text)
        if fallback:
            return json.dumps(fallback, indent=2)
        return f"⚠️ Invalid JSON generated (parse error: {str(e)}):\n\n{result}"
    except Exception as e:
        return f"⚠️ Error processing response: {str(e)}\n\n{result}"


# 🔹 Gradio UI
interface = gr.Interface(
    fn=extract_json,
    inputs=gr.Textbox(
        lines=10, 
        placeholder="Paste invoice text here...",
        label="Invoice Text"
    ),
    outputs=gr.Textbox(
        lines=15,
        label="Extracted JSON"
    ),
    title="🧾 Invoice JSON Extractor",
    description="Paste unstructured invoice text → Get structured JSON output",
    examples=[
        ["Vendor: Amazon\nDate: 2024-03-10\nTotal: 2500 INR\nItems: Server charges"],
        ["Invoice #12345\nFrom: Acme Corp\nAmount: $1,500\nDue: April 1, 2024"],
    ]
)

if __name__ == "__main__":
    share = os.getenv("GRADIO_SHARE", "false").lower() in {"1", "true", "yes"}
    server_port = int(os.getenv("PORT", "7860"))
    try:
        interface.launch(
            server_name="0.0.0.0",
            server_port=server_port,
            share=share,
        )
    except ValueError:
        interface.launch(
            server_name="0.0.0.0",
            server_port=server_port,
            share=True,
        )
