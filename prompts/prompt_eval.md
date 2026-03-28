# Prompt-Only Evaluation on 3 Worst Baseline Documents

| document    | v1 parse success | v2 parse success | v3 parse success | v4 parse success | best notes                              |
| ----------- | ---------------: | ---------------: | ---------------: | ---------------: | --------------------------------------- |
| eval_doc_01 |                0 |                1 |                1 |                1 | v2+ removed markdown fences             |
| eval_doc_07 |                0 |                0 |                0 |                0 | trailing comma persisted intermittently |
| eval_doc_15 |                0 |                0 |                1 |                1 | v3+ forced strict JSON object           |

## Aggregate on this 3-doc subset

- Best prompt-only parse success: 2/3 = 66.7%
- Fine-tuned model parse success on same 3 docs: 3/3 = 100.0%

## Observations

- Prompt strengthening can reduce formatting noise for simpler cases.
- Persistent structural issues (for example trailing comma generation) are not reliably fixed by prompt edits alone.
- Few-shot examples help, but behavior remains less stable than fine-tuning for strict machine parsing.
