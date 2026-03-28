# Structured Output Fine-Tuning for Reliable JSON Extraction

This repository contains a complete project submission for fine-tuning Llama 3.2 with LoRA to improve machine-parseable JSON extraction from invoices and purchase orders.

## Project Goal

Improve extraction reliability from unstructured business documents by maximizing parse success rate under a fixed JSON schema.

## Repository Structure

- `schema/`
  - `invoice_schema.md`
  - `po_schema.md`
- `data/`
  - `curated_train.jsonl` (80 examples)
  - `curation_log.md`
- `training_config.md`
- `screenshots/`
  - `training_config.png`
  - `loss_curve.png`
- `eval/`
  - `baseline_responses.md`
  - `baseline_scores.csv`
  - `summary.md`
  - `finetuned_responses.md`
  - `finetuned_scores.csv`
  - `before_vs_after.md`
  - `failures/failure_01.md` to `failure_05.md`
- `prompts/`
  - `prompt_iterations.md`
  - `prompt_eval.md`
- `report.md`

## Methodology

1. Defined strict JSON schemas for invoice and PO extraction.
2. Curated 80 high-diversity training examples in JSONL format.
3. Established baseline performance on 20 held-out documents.
4. Configured and ran LoRA SFT via LlamaFactory UI.
5. Re-evaluated on the same held-out set for fair ablation.
6. Performed targeted failure analysis on 5 residual errors.
7. Compared prompt-only optimization vs fine-tuning.

## Key Results

- Baseline parse success rate: **40.0%**
- Post fine-tuning parse success rate: **90.0%**
- Major reduction in formatting failures (markdown fences/prose wrappers).

## Notes

- This repository excludes model binaries and adapter weights by design.
- Evaluation artifacts are provided in documented, auditable markdown/CSV files.
