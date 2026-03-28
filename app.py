from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr
import torch
import json
import os

# 🔹 Load model
# Update this path to your model folder
model_path = os.getenv("MODEL_PATH", "./model")

print(f"Loading model from: {model_path}")

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("✅ Model loaded successfully")


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

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.1,
        top_p=0.9,
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

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
    title="🧾 Invoice JSON Extractor (Llama 3.2)",
    description="Paste unstructured invoice text → Get structured JSON output",
    examples=[
        ["Vendor: Amazon\nDate: 2024-03-10\nTotal: 2500 INR\nItems: Server charges"],
        ["Invoice #12345\nFrom: Acme Corp\nAmount: $1,500\nDue: April 1, 2024"],
    ]
)

if __name__ == "__main__":
    interface.launch(share=False)
