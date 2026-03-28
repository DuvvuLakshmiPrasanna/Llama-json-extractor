# Architecture & Technical Design

## System Architecture

```
Input Layer (Text/PDF)
    ↓
Preprocessing & Tokenization
    ↓
Model Inference (Fine-tuned Llama 3.2)
    ↓
JSON Extraction & Validation
    ↓
Output (Structured JSON)
```

## Component Design

### 1. Model Loading Component

**Purpose**: Initialize and manage model lifecycle

```python
class ModelManager:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def generate(self, prompt, max_tokens=300):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.1
        )
        return self.tokenizer.decode(outputs[0])
```

### 2. Inference Component

**Purpose**: Execute model inference with error handling

```python
class InferenceEngine:
    def __init__(self, model_manager):
        self.model = model_manager

    def extract_json(self, text):
        prompt = f"Extract JSON: {text}"
        try:
            output = self.model.generate(prompt)
            return self._parse_json(output)
        except Exception as e:
            return self._handle_error(e)

    def _parse_json(self, text):
        json_start = text.find("{")
        json_end = text.rfind("}") + 1
        return json.loads(text[json_start:json_end])
```

### 3. Validation Component

**Purpose**: Validate outputs against schema

```python
class SchemaValidator:
    def __init__(self, schema_path):
        self.schema = self._load_schema(schema_path)

    def validate(self, json_obj):
        errors = []
        for field, rules in self.schema.items():
            if field not in json_obj and rules.get("required"):
                errors.append(f"Missing required field: {field}")
        return len(errors) == 0, errors
```

### 4. Web Interface Component

**Purpose**: Provide user-friendly interaction layer

```python
interface = gr.Interface(
    fn=extract_json,
    inputs=[
        gr.Textbox(lines=10, label="Invoice Text"),
        gr.Slider(0, 1, value=0.1, label="Temperature")
    ],
    outputs=gr.Textbox(lines=15, label="JSON Output"),
    title="Invoice JSON Extractor",
    description="Extract structured data from invoices"
)
```

## Data Flow

### Inference Pipeline

```
User Text Input
    ↓
[Tokenize] → Convert to token IDs
    ↓
[Embed] → Create embeddings
    ↓
[LoRA Adapters] → Apply domain-specific knowledge
    ↓
[Generate Tokens] → Model inference (temperature=0.1)
    ↓
[Decode] → Convert tokens to text
    ↓
[Extract JSON Section] → Find {} boundaries
    ↓
[Validate] → Check schema compliance
    ↓
Valid JSON → User Output
OR
Parse Error → Fallback with explanation
```

### Training Pipeline

```
JSONL Data
    ↓
[Load & Parse] → 80 training examples
    ↓
[Tokenize] → Convert to model input
    ↓
[Initialize LoRA] → Create rank-8 adapters
    ↓
[Freeze Base Model] → Keep Llama weights fixed
    ↓
[Fine-tune LoRA] → 3 epochs optimization
    ↓
[Validate on Holdout] → 20 test documents
    ↓
Monitor Loss → Training/Validation curves
    ↓
[Merge] → Combine LoRA into base model
    ↓
Deployment Model
```

## Performance Characteristics

### Inference Speed

| Configuration       | Speed            | Memory |
| ------------------- | ---------------- | ------ |
| GPU (V100, float16) | ~0.5-1.0 seconds | ~8GB   |
| GPU (A100, float16) | ~0.3-0.5 seconds | ~8GB   |
| GPU (T4, float16)   | ~1-2 seconds     | ~8GB   |
| CPU (Intel i9)      | ~5-10 seconds    | ~4GB   |

### Memory Requirements

```
Model Loading:
  - Base Llama model: ~14GB (7B @ float16)
  - LoRA adapters: ~50MB
  - Tokenizer: ~1MB
  - Total: ~14GB GPU VRAM

Inference:
  - Batch size 1: ~8GB
  - Batch size 4: ~12GB
  - Batch size 8: ~16GB
```

### Optimization Techniques

1. **Float16 Precision**: Reduces memory 50% vs float32
2. **Device Map "auto"**: Optimizes GPU/CPU placement
3. **Token Limiting**: max_new_tokens=300 bounds computation
4. **Low Temperature**: Less sampling overhead

## Scalability Considerations

### Horizontal Scaling

```
Load Balancer
    ↓
[Server 1: Inference Worker]
[Server 2: Inference Worker]
[Server 3: Inference Worker]
[Server 4: Inference Worker]
    ↓
Shared Cache (Redis)
    ↓
Result Database
```

### Vertical Scaling

1. Use larger GPU (A100 > V100 > T4)
2. Increase batch size (if memory allows)
3. Multi-GPU setup with distributed inference
4. Model quantization (INT8) for 2x speedup

## Deployment Options

### Single Server

```
┌──────────────────┐
│  Web Interface   │ (Gradio)
├──────────────────┤
│   Inference      │ (PyTorch)
├──────────────────┤
│   Model Files    │ (Filesystem)
└──────────────────┘
```

### Cloud Deployment (HF Spaces)

```
User → [HF Spaces] → [Gradio Interface] → [Model Inference] → Result
```

### Enterprise Deployment

```
Client Applications
        ↓
[API Gateway]
        ↓
[Load Balancer]
        ↓
[Inference Server Pool]
        ↓
[Model Cache]
        ↓
[Result Database]
```

## Error Handling Strategy

### Layer 1: Input Validation

- Check text input is not empty
- Limit input length to prevent OOM
- Validate encoding

### Layer 2: Inference Safety

- GPU memory checks
- Timeout detection
- Exception catching

### Layer 3: Output Validation

- JSON parsing with error recovery
- Schema validation
- Field type checking

### Layer 4: User Feedback

- Clear error messages
- Suggestions for recovery
- Logging for debugging

## Testing Strategy

### Unit Tests

```python
def test_json_extraction():
    result = extract_json("Vendor: Acme, Total: $1000")
    assert "vendor" in result
    assert result["total"] == 1000

def test_schema_validation():
    validator = SchemaValidator("invoice_schema.md")
    assert validator.validate(valid_invoice)[0]
    assert not validator.validate(invalid_invoice)[0]
```

### Integration Tests

```python
def test_end_to_end():
    app = create_app()
    response = app.call(extract_json, "Invoice text")
    assert response["status"] == "success"
    assert response["data"]["vendor"] is not None
```

### Performance Tests

```python
def test_inference_speed():
    start = time.time()
    extract_json("Test input")
    elapsed = time.time() - start
    assert elapsed < 5.0  # Must be <5 seconds
```

## Security Considerations

### Input Sanitization

- Sanitize user input to prevent injection
- Validate file uploads
- Limit input size

### Model Security

- Don't expose model weights directly
- Use signed URLs for model uploads
- Rate limit API endpoints

### Data Privacy

- Don't log sensitive data
- Encrypt data in transit
- Implement access controls

## Monitoring & Observability

### Metrics to Track

1. **Performance Metrics**
   - Inference latency (p50, p95, p99)
   - Throughput (requests/second)
   - GPU utilization
   - Memory usage

2. **Quality Metrics**
   - JSON parse success rate
   - Schema validation accuracy
   - Error distribution
   - User feedback scores

3. **System Metrics**
   - Server uptime
   - Error rates
   - Request queue length
   - Model cache hit rate

### Logging Strategy

```python
logging.info(f"Processing invoice {invoice_id}")
logging.debug(f"Generated tokens: {tokens}")
logging.warning(f"Parse failure on {invoice_id}, attempting recovery")
logging.error(f"Critical error: {error_message}", exc_info=True)
```

---

**This document provides the blueprint for the system architecture and design decisions.**
