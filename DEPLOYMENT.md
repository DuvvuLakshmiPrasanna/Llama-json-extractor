# 🚀 Deployment Guide: Invoice JSON Extractor

Complete step-by-step guide to deploy your fine-tuned Llama 3.2 model with a web interface.

---

## 📋 Prerequisites

- ✅ Fine-tuned Llama 3.2 model (merged or with LoRA adapter)
- ✅ Python 3.10+
- ✅ GPU strongly recommended (can use CPU for demos)

---

## 🟢 PHASE 1: Prepare Your Model

### Option A: Merge Model + LoRA (Recommended)

If you trained with LoRA in LlamaFactory:

1. **In LlamaFactory UI:**
   - Go to **"Export / Merge"**
   - Select your checkpoint
   - Click **"Export"**

2. **Output folder structure:**
   ```
   my-llama-json-model/
   ├── config.json
   ├── tokenizer.json
   ├── tokenizer_config.json
   ├── pytorch_model.bin (or safetensors)
   ├── special_tokens_map.json
   └── generation_config.json
   ```

### Option B: Use Existing Model

If already merged or downloaded:

- Ensure all files above are present
- Test with: `transformers-cli env`

✅ **Save this folder path** — you'll need it for deployment.

---

## 🟢 PHASE 2: Test Locally

### Step 1: Install Dependencies

```bash
cd llama-json-extractor
pip install -r requirements.txt
```

### Step 2: Run App

```bash
python app.py
```

### Step 3: Test in Browser

- **URL:** `http://127.0.0.1:7860`
- **Test Input:**

  ```
  Vendor: Amazon
  Invoice Date: March 10, 2024
  Order ID: ORD-12345
  Total Amount: $2,500
  Status: Paid
  ```

- **Expected Output:**
  ```json
  {
    "vendor": "Amazon",
    "date": "2024-03-10",
    "order_id": "ORD-12345",
    "total": "$2,500",
    "status": "Paid"
  }
  ```

✅ If JSON output appears → Ready for deployment!

---

## 🌐 PHASE 3: Deploy Online (FREE)

### Best Option: Hugging Face Spaces

**Why?**

- ✅ Free GPU tier
- ✅ Simple deployment
- ✅ No credit card needed
- ✅ Public/Private options

### Step 1: Create Hugging Face Account

👉 https://huggingface.co/join

### Step 2: Create New Space

1. Click **"New Space"** → https://huggingface.co/new
2. Fill form:
   - **Space name:** `llama-json-extractor`
   - **Space type:** Select **Gradio**
   - **License:** Optional (choose any or skip)
   - **Visibility:** Public or Private
3. Click **"Create"**

### Step 3: Set Up Git Repo

```bash
# Clone the space
git clone https://huggingface.co/spaces/yourusername/llama-json-extractor
cd llama-json-extractor

# Copy your files
cp /path/to/app.py .
cp /path/to/requirements.txt .

# Push to HF
git add .
git commit -m "Initial deployment"
git push
```

### Step 4: Upload Model

**Option A: Small Model (<2GB)**

```bash
git lfs install
git add -A
git commit -m "Add model"
git push
```

**Option B: Large Model or Use Hugging Face Model Hub**

Reference a public model in `app.py`:

```python
model_path = "meta-llama/Llama-2-7b-hf"  # Use public model
```

Or upload your model to your HF profile:

```bash
huggingface-cli upload yourusername/llama-json-model . --repo-type model
```

Then update `app.py`:

```python
model_path = "yourusername/llama-json-model"
```

### Step 5: Verify Deployment

✅ Your app is live at:

```
https://huggingface.co/spaces/yourusername/llama-json-extractor
```

---

## 📦 PHASE 4: If Model is Too Large

### Use API Alternative

Replace inference in `app.py`:

```python
import requests

def extract_json(text):
    # Use Together AI
    response = requests.post(
        "https://api.together.xyz/inference",
        json={
            "model": "meta-llama/Llama-2-7b-chat",
            "prompt": f"Extract JSON from: {text}",
            "max_tokens": 300,
        },
        headers={"Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}"}
    )
    return response.json()["output"]["choices"][0]["text"]
```

**Free API Options:**

- **Together AI:** https://together.ai (free credits)
- **Replicate:** https://replicate.com (pay-as-you-go)
- **Hugging Face Inference:** https://huggingface.co/inference-api

---

## 🛠️ PHASE 5: Improve Reliability

### 1. Stricter Prompt Engineering

```python
prompt = f"""You are an invoice extraction expert. Extract all relevant fields.
Return ONLY valid JSON. Do not include:
- Markdown formatting
- Explanations
- Extra text
- Backticks

Invoice:
{text}

JSON output:"""
```

### 2. Add JSON Validation

```python
def validate_and_format(json_str):
    try:
        parsed = json.loads(json_str)
        # Add schema validation here
        return json.dumps(parsed, indent=2)
    except:
        return None
```

### 3. Error Handling

```python
try:
    result = extract_json(text)
except torch.cuda.OutOfMemoryError:
    return "❌ Out of GPU memory - try shorter input"
except Exception as e:
    return f"❌ Error: {str(e)}"
```

---

## ✨ PHASE 6: Add Extra Features (Optional)

### Feature 1: File Upload

```python
interface = gr.Interface(
    fn=extract_json,
    inputs=[
        gr.File(label="Upload Text File"),  # NEW
        gr.Textbox(label="Or paste text")
    ],
    outputs=gr.Textbox(label="JSON Output"),
)
```

### Feature 2: Download JSON

```python
outputs = [
    gr.Textbox(label="JSON Output"),
    gr.File(label="Download JSON")  # NEW
]
```

### Feature 3: Batch Processing

```python
def extract_batch(csv_file):
    results = []
    for row in csv_file:
        results.append(extract_json(row["text"]))
    return gr.dataframe(results)
```

### Feature 4: Confidence Scores

```python
def extract_with_confidence(text):
    json_output = extract_json(text)
    confidence = model_confidence(text, json_output)
    return {
        "json": json_output,
        "confidence": confidence
    }
```

---

## 📊 Monitoring & Metrics

### Add Usage Logging

```python
import logging

logging.basicConfig(filename="usage.log", level=logging.INFO)

def extract_json(text):
    logging.info(f"Input length: {len(text)}")
    result = extract_json_impl(text)
    logging.info(f"Output: {result[:50]}...")
    return result
```

---

## 🐛 Troubleshooting

| Issue              | Solution                                          |
| ------------------ | ------------------------------------------------- |
| Model not loading  | Check path, reinstall `transformers`              |
| Out of memory      | Use `device_map="cpu"` or reduce `max_new_tokens` |
| GPU not detected   | Run `python -m torch.utils.collect_env`           |
| JSON parsing fails | Add fallback schema validation                    |
| Slow response      | Use quantization (INT8) or smaller model          |
| HF Space timeout   | Upload model to HF Hub, reference by ID           |

---

## 📱 Demo Flow for Presentation

1. **Show the app** → `https://huggingface.co/spaces/yourname/llama-json-extractor`
2. **Paste sample invoice:**
   ```
   Invoice #INV-2024-001
   Date: March 15, 2024
   Customer: Acme Corp
   Items: Software licenses (3) @ $500 each
   Tax: 10%
   Total: $1,650
   ```
3. **Click Submit** → Get JSON:
   ```json
   {
     "invoice_number": "INV-2024-001",
     "date": "2024-03-15",
     "customer": "Acme Corp",
     "items": [
       { "description": "Software licenses", "quantity": 3, "price": 500 }
     ],
     "tax": "10%",
     "total": 1650
   }
   ```
4. **Show error handling** → Paste bad data → See graceful fallback

---

## ✅ Submission Checklist

- [ ] Model trained and merged
- [ ] `app.py` runs locally without errors
- [ ] JSON output is valid on test inputs
- [ ] Deployed to Hugging Face Spaces (or similar)
- [ ] Public URL is shareable
- [ ] README.md explains the project
- [ ] Added example invoices/test cases
- [ ] Error handling works (bad input → graceful message)

---

## 🎉 You're Done!

Your deployment includes:

```
Frontend (Gradio UI)
        ↓
LLM Inference (Llama 3.2 Fine-tuned)
        ↓
JSON Extraction & Validation
        ↓
Structured Output
```

**Ready to show evaluators!** ✨

---

## 📚 Additional Resources

- **Gradio Docs:** https://gradio.app/docs
- **Transformers:** https://huggingface.co/docs/transformers
- **Hugging Face Spaces:** https://huggingface.co/spaces
- **LlamaFactory:** https://github.com/hiyouga/LlamaFactory

---

## 💡 Next Steps

Want to improve further?

1. **Add PDF/Image Support:** Use OCR (Tesseract, PaddleOCR)
2. **Schema Validation:** Validate JSON against predefined schema
3. **Multi-model Support:** Load multiple fine-tuned variants
4. **Analytics Dashboard:** Track usage, errors, performance
5. **Mobile App:** Build Flutter/React Native wrapper

Feel free to reach out! 🚀
