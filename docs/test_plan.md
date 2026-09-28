# BluePeak Test Plan

## Formative testing
Validate normalization, risk scoring, ATT&CK mapping, recommendation generation, output creation, and human-review controls with controlled inputs. Record defects and retest after correction.

## Summative testing
Process the full 15-alert controlled dataset end to end and compare actual outputs against `data/expected_results.json`.

## Acceptance criteria
- 100% valid alert processing
- >=95% required-field normalization accuracy
- >=90% priority accuracy
- >=90% ATT&CK mapping accuracy for applicable scenarios
- 100% human-review enforcement
- 100% result capture

## Final Refinement Tests

Before summative evaluation, the lab adds negative-input testing for missing required fields and unsupported severity values. Invalid inputs must be rejected, the reason must be recorded, and no risk decision may be generated for the rejected alert. The evaluator also derives processing, normalization, prioritization, ATT&CK mapping, human-review, and result-capture KPIs from actual result objects rather than fixed percentages.
