\# Test Case Documentation – Yuno Payment Automation



\## Purchase Payment

| Test Case | Description | Type | Expected Result |

|-----------|-------------|------|----------------|

| Minimal Fields | Purchase with only required fields | Sanity, Regression | Status 201, payment SUCCEEDED |

| Maximal Fields | Purchase with customer\_payer and additional\_data | Regression, Integration | Status 201, customer details present |

| Invalid Card | Purchase with invalid card number | Negative, Regression | Status 400, error returned |



\## Authorization Payment

| Test Case | Description | Type | Expected Result |

|-----------|-------------|------|----------------|

| Minimal Fields | Authorize with required fields | Sanity, Regression | Status 201, authorization AUTHORIZED |

| Maximal Fields | Authorize with additional data | Regression | Status 201 |

| Invalid Amount | Authorize with invalid amount | Negative, Regression | Status 400, error returned |



\## Refund Payment

| Test Case | Description | Type | Expected Result |

|-----------|-------------|------|----------------|

| Full Refund | Refund full amount of successful payment | Regression | Status 201, refund SUCCEEDED |

| Invalid Payment ID | Refund with wrong payment ID | Negative, Regression | Status 404, error returned |



\## Verify Payment

| Test Case | Description | Type | Expected Result |

|-----------|-------------|------|----------------|

| Valid Card | Verify payment with valid card | Sanity, Regression | Status 201 |

| Invalid Card | Verify payment with invalid card | Negative, Regression | Status 400, error returned |



\## Edge Cases

\- Invalid card numbers

\- Refund with wrong payment ID

\- Authorization with invalid amounts

\- Verify flow with invalid card



