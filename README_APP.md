# Llama JSON Extractor - Deployment Ready

This project provides a **complete, production-ready deployment** of a fine-tuned Llama 3.2 model for extracting structured JSON from unstructured invoice text.

## 🎯 Quick Start

### Local Testing (5 minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open browser to http://127.0.0.1:7860
```

### Deploy Online (15 minutes)

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete Hugging Face Spaces setup guide.

---

## 📂 Project Structure

```
llama-json-extractor/
├── app.py                    # Gradio web app with model inference
├── requirements.txt          # Python dependencies
├── DEPLOYMENT.md             # Complete deployment guide
├── README.md                 # This file
├── data/                     # Training data
│   └── curated_train.jsonl
├── eval/                     # Evaluation results
│   ├── baseline_scores.csv
│   ├── finetuned_scores.csv
│   └── failures/
├── prompts/                  # Prompt engineering iterations
└── schema/                   # Invoice schema definitions
```

---

## 🔧 How It Works

1. **User inputs** unstructured invoice text
2. **Llama 3.2 model** (fine-tuned on invoice data) processes it
3. **App extracts JSON** and validates output
4. **JSON displayed** in web interface

### Example

**Input:**

```
Vendor: Amazon
Invoice Date: March 10, 2024
Total: $2,500
Status: Paid
```

**Output:**

```json
{
  "vendor": "Amazon",
  "invoice_date": "2024-03-10",
  "total": "$2,500",
  "status": "Paid"
}
```

---

## 🚀 Deployment Options

| Option                  | Effort       | Cost        | Speed     |
| ----------------------- | ------------ | ----------- | --------- |
| **Hugging Face Spaces** | ⭐ Easy      | Free        | Fast      |
| **Gradio Share Link**   | ⭐ Very Easy | Free        | Temporary |
| **AWS/GCP Cloud**       | ⭐⭐⭐ Hard  | Paid        | Fast      |
| **Replicate API**       | ⭐⭐ Medium  | Pay-per-use | Very Fast |

**Recommended:** Hugging Face Spaces (see [DEPLOYMENT.md](DEPLOYMENT.md))

---

## 📊 Model Details

- **Base Model:** Llama 3.2 (7B)
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **Training Data:** Curated invoice dataset
- **Task:** Invoice field extraction → JSON format
- **Inference Time:** ~2-5 seconds per invoice
- **Requirements:** 16GB+ GPU (or use CPU for demos)

---

## 🔍 Features

✅ **Web UI** - Simple, intuitive interface (Gradio)
✅ **JSON Validation** - Ensures valid output
✅ **Error Handling** - Graceful fallback on invalid generation
✅ **Examples** - Pre-loaded test cases
✅ **Shareable** - Deploy and share link
✅ **Scalable** - Easy to add batch processing

---

## 📈 Evaluation Results

See [eval/summary.md](eval/summary.md) for:

- Baseline vs fine-tuned comparison
- Accuracy metrics
- Failure analysis
- Performance improvements

**Key Finding:** Fine-tuned model achieves **~85% F1 score** on invoice extraction

---

## 🛠️ Configuration

### Model Path

Update `app.py` line 8:

```python
model_path = "./model"  # Path to your model folder
```

### Inference Parameters

Adjust in `app.py`:

```python
outputs = model.generate(
    **inputs,
    max_new_tokens=300,      # Increase for longer invoices
    temperature=0.1,          # Lower = deterministic, Higher = creative
    top_p=0.9,
)
```

---

## 🐛 Troubleshooting

### Model Not Loading

```bash
python -c "from transformers import AutoModel; AutoModel.from_pretrained('your_model_path')"
```

### Out of GPU Memory

- Reduce `max_new_tokens` to 150
- Use `device_map="cpu"` (slower)
- Use quantized version (INT8)

### Slow Response

- Enable half-precision (already set: `torch.float16`)
- Reduce batch size or input length
- Use GPU instead of CPU

### Invalid JSON Output

1. Check prompt engineering
2. Increase `temperature` to 0.3
3. Fine-tune model with more examples

---

## 📚 Learn More

- [LlamaFactory Docs](https://github.com/hiyouga/LlamaFactory)
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Gradio Tutorial](https://gradio.app/quickstart/)
- [DEPLOYMENT.md](DEPLOYMENT.md) - Detailed deployment guide
- [eval/summary.md](eval/summary.md) - Model performance metrics

---

## 🎓 Use Cases

✅ Automated invoice processing
✅ Document parsing  
✅ Data extraction from forms
✅ Expense management automation
✅ Supply chain optimization

---

## 📝 License

MIT License (see LICENSE if present)

---

## 🤝 Support

For deployment help:

1. Check [DEPLOYMENT.md](DEPLOYMENT.md)
2. Review error messages in terminal
3. Test with simpler prompts first
4. Check model loading step-by-step

---

**Status:** ✅ Ready for submission & deployment

**Next:** Follow [DEPLOYMENT.md](DEPLOYMENT.md) to go live! 🚀
