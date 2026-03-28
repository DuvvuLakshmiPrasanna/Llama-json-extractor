# Training Configuration (LlamaFactory UI)

## Model and method

- Base model: `Llama-3.2-3B-Instruct`
- Fine-tuning method: `LoRA`
- Task type: Supervised fine-tuning (SFT) for structured extraction
- Dataset: `data/curated_train.jsonl` (80 examples: 50 invoices, 30 purchase orders)

## Hyperparameters and justifications

- LoRA rank (`r`): `16`
  Reason: Moderate-capacity adapter balances expressiveness and overfitting risk for a small 80-example dataset; rank 8 was slightly underfit in early tests, while 32 over-parameterized for this scale.

- LoRA alpha: `32`
  Reason: Standard practice is alpha = 2 x rank, giving stable effective update scaling.

- Learning rate: `2e-4`
  Reason: Falls in the practical LoRA range (1e-4 to 3e-4), converged smoothly without unstable spikes.

- Epochs: `3`
  Reason: Loss plateaued by late epoch 2; epoch 3 improved format consistency while avoiding heavy memorization.

- Per-device batch size: `2`
  Reason: Highest stable batch size on local hardware with no OOM conditions.

- Gradient accumulation steps: `8`
  Reason: Effective batch size of 16 improves gradient stability on small data.

- Max sequence length: `2048`
  Reason: Captures full raw document text and JSON output for longer invoice/PO layouts.

- Warmup ratio: `0.1`
  Reason: Prevents early optimization shock on adapter layers.

- Weight decay: `0.0`
  Reason: Standard LoRA setting for adapter-only optimization.

- LR scheduler: `cosine`
  Reason: Smooth decay benefited late-epoch formatting consistency.

- Precision: `fp16`
  Reason: Reduced memory footprint and improved throughput on supported hardware.

## Run notes

### Run 1

- Config: r=8, alpha=16, lr=2e-4, epochs=3
- Observation: Improved key presence but still frequent markdown fences.
- Action: Increased rank to 16.

### Run 2 (selected)

- Config: r=16, alpha=32, lr=2e-4, epochs=3
- Observation: Steady loss decline and improved JSON formatting reliability.
- Selection rationale: Best parse success on held-out validation prompts.

## Loss curve interpretation

- Loss decreased smoothly during epoch 1 and early epoch 2.
- Curve flattened through epoch 3, indicating convergence.
- No sudden collapse to near-zero loss in epoch 1, suggesting overfitting risk remained controlled.

## Screenshots

- Training configuration panel: `screenshots/training_config.png`
- Final loss curve: `screenshots/loss_curve.png`
