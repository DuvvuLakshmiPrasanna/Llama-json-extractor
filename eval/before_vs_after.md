# Before vs After Fine-Tuning

| metric                           | baseline (base model) | post fine-tuning |
| -------------------------------- | --------------------: | ---------------: |
| parse success rate               |          40.0% (8/20) |    90.0% (18/20) |
| avg key accuracy                 |                 0.696 |            0.989 |
| avg value accuracy               |                 0.546 |            0.881 |
| responses with markdown fences   |                     1 |                0 |
| responses with prose preamble    |                     3 |                0 |
| responses with wrong schema keys |                     7 |                1 |

## Notes

- Fine-tuning sharply reduced formatting failures (fences, prose, malformed key names).
- Remaining errors are concentrated in edge cases: trailing comma, missing nested array key, and numeric type drift.
- The largest production impact is parse reliability (40% to 90%), which directly reduces downstream parser failures.
