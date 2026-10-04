# Precedent Loom

An exception is not fair merely because it cites a rule. It must also explain why materially similar cases did not receive a different answer.

Precedent Loom freezes a public policy and a closed list of rule labels. Applicants file requests from a separate source origin. GenLayer validators fetch the unchanged policy and the new request, identify every material rule, locate semantically similar finalized cases, and return a bounded decision. Contract code compares the new decision with those analogues. A consistent case becomes `FINAL`; a conflicting one stops at `RECONCILIATION` instead of silently joining the record.

The evolving casebook is the primitive. Earlier request excerpts, decisions, rule indexes, and source digests become the comparison set for later cases. The contract rejects duplicate IDs, same-origin policy and request sources, policy mutation, and replayed evaluation.

## Lifecycle

`BOOK OPEN -> CASE FILED -> FINAL | RECONCILIATION`

## Verify

```text
genvm-lint check contracts/contract.py
python -m pytest -q
```

Evidence files are operator-created fixtures for a technical network rehearsal. Separate hosts demonstrate source-slot behavior, not independent institutional authority.

