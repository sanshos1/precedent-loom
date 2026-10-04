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

## StudioNet proof

- Contract: [`0x5CadFE0a5f80855c5afFB6C2D4912d2b5c36BB29`](https://explorer-studio.genlayer.com/address/0x5CadFE0a5f80855c5afFB6C2D4912d2b5c36BB29)
- Deployment: [`0x701b987a53c0cb7fc9d03c076df553860fda379b32dd5b7f4ce24c17a73a4818`](https://explorer-studio.genlayer.com/transactions/0x701b987a53c0cb7fc9d03c076df553860fda379b32dd5b7f4ce24c17a73a4818)
- Live evaluation: [`0x4da3c92fea7f881dff68ab05b404d52f22c2b2dabe7e40349d223f98b8c94c47`](https://explorer-studio.genlayer.com/transactions/0x4da3c92fea7f881dff68ab05b404d52f22c2b2dabe7e40349d223f98b8c94c47)
- Result: `ACCESS-1791072846:EAST-1791072846`, `GRANT`, `FINAL`
- Deployed source SHA-256: `de3bde3ffbbf39b1427f53584ad6d3c5aaaa384f8f85bc3794f4b0b6198573cd`, exact match.

