from transformers import pipeline
import gradio as gr
import json
import os

# Use open models by default so Spaces starts without auth tokens.
requested_model_id = os.getenv("MODEL_ID", "google/flan-t5-base")
fallback_model_ids = [
    requested_model_id,
    "google/flan-t5-base",
    "google/flan-t5-small",
]

pipe = None
loaded_model_id = None
last_error = None

for candidate in fallback_model_ids:
    try:
        print(f"Loading model: {candidate}")
        pipe = pipeline(
            "text2text-generation",
            model=candidate,
            device_map="auto",
        )
        loaded_model_id = candidate
        break
    except Exception as err:
        last_error = err
        print(f"Model load failed for {candidate}: {err}")

if pipe is None:
    raise RuntimeError(
        "Unable to load any supported model. "
        f"Last error: {last_error}"
    )

print(f"Model loaded successfully: {loaded_model_id}")


# 🔹 Prediction function
def extract_json(text):
    """
    Extract structured invoice data from unstructured text.
    Converts raw invoice text to valid JSON format.
    """
    
    prompt = f"""Extract invoice data and return ONLY valid JSON. Do not include explanation, markdown, or extra text.

Invoice text:
{text}

Return valid JSON only:"""

    outputs = pipe(
        prompt,
        max_new_tokens=300,
        temperature=0.1,
        top_p=0.9,
    )

    result = outputs[0]["generated_text"]

    # 🔹 Try to clean and parse JSON
    try:
        json_start = result.find("{")
        json_end = result.rfind("}") + 1
        
        if json_start == -1 or json_end == 0:
            return "⚠️ No JSON found in response:\n\n" + result
        
        json_str = result[json_start:json_end]
        parsed = json.loads(json_str)
        return json.dumps(parsed, indent=2)
    
    except json.JSONDecodeError as e:
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
    interface.launch(share=False)
