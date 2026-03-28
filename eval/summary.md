# Evaluation Summary

## Baseline Parse Success Rate

**8 / 20 = 40.0%**

Definition used:

parse success rate = (is_valid_json = true AND has_all_required_keys = true) / total responses

Counts from `eval/baseline_scores.csv`:

- Total evaluated responses: 20
- Valid JSON responses: 14
- Responses with all required keys: 8
- Responses satisfying both conditions: 8

Interpretation:

The base model can often identify relevant content, but output formatting and schema consistency are unreliable for production parsing pipelines.
