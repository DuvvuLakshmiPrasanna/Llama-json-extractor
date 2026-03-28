# 🚀 Quick Reference Card

## Local Testing (3 steps)

```bash
# Step 1: Setup
./setup.sh           # macOS/Linux
setup.bat            # Windows

# Step 2: Run
python app.py

# Step 3: Test
# Open: http://127.0.0.1:7860
```

## Deploy to Hugging Face Spaces (5 steps)

1. **Create Space**
   - Go to https://huggingface.co/new
   - Select "Gradio" SDK
   - Click "Create"

2. **Push Code**

   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/llama-json-extractor
   cd llama-json-extractor
   cp app.py requirements.txt .
   git add .
   git commit -m "Add app"
   git push
   ```

3. **Upload Model**
   - Place model folder in space, OR
   - Reference public model in `app.py`

4. **Wait for Build**
   - Space builds automatically
   - Check logs if errors appear

5. **Share Link**
   ```
   https://huggingface.co/spaces/YOUR_USERNAME/llama-json-extractor
   ```

## Troubleshooting

| Problem           | Fix                                 |
| ----------------- | ----------------------------------- |
| Model not loading | Verify path in `app.py` line 8      |
| Out of memory     | Reduce `max_new_tokens` to 150      |
| Slow generation   | Use GPU instead of CPU              |
| Invalid JSON      | Check prompt in `app.py` line 28-32 |
| HF Space timeout  | Use public model from Hub           |

## File Reference

| File                     | Purpose                 |
| ------------------------ | ----------------------- |
| `app.py`                 | Main Gradio application |
| `requirements.txt`       | Python dependencies     |
| `setup.sh` / `setup.bat` | Quick environment setup |
| `DEPLOYMENT.md`          | Complete guide          |
| `README_APP.md`          | Project overview        |
| `.gitignore`             | Git ignore rules        |

## Test Input

```
Vendor: Acme Corp
Invoice Date: March 1, 2024
Order ID: ORD-2024-001
Amount: $5,000
Status: Pending
```

## Expected Output

```json
{
  "vendor": "Acme Corp",
  "invoice_date": "2024-03-01",
  "order_id": "ORD-2024-001",
  "amount": "$5,000",
  "status": "Pending"
}
```

## Useful Links

- [DEPLOYMENT.md](DEPLOYMENT.md) - Full deployment guide
- [README_APP.md](README_APP.md) - Project details
- [HF Spaces Docs](https://huggingface.co/docs/hub/spaces)
- [Gradio Docs](https://gradio.app/docs)

---

**Status:** ✅ Ready to deploy!
