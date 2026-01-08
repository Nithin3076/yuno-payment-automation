Test Case Documentation – Yuno Payment Automation

Purchase Payment



Test Case: Minimal Fields

Description: Purchase with only required fields

Type: Sanity, Regression

Expected Result: Status 201, payment SUCCEEDED



Test Case: Maximal Fields

Description: Purchase with customer\_payer and additional\_data

Type: Regression, Integration

Expected Result: Status 201, customer details present



Test Case: Invalid Card

Description: Purchase with invalid card number

Type: Negative, Regression

Expected Result: Status 400, error returned



Authorization Payment



Test Case: Minimal Fields

Description: Authorize with required fields

Type: Sanity, Regression

Expected Result: Status 201, authorization AUTHORIZED



Test Case: Maximal Fields

Description: Authorize with additional data

Type: Regression

Expected Result: Status 201



Test Case: Invalid Amount

Description: Authorize with invalid amount

Type: Negative, Regression

Expected Result: Status 400, error returned



Refund Payment



Test Case: Full Refund

Description: Refund full amount of successful payment

Type: Regression

Expected Result: Status 201, refund SUCCEEDED



Test Case: Invalid Payment ID

Description: Refund with wrong payment ID

Type: Negative, Regression

Expected Result: Status 404, error returned



Verify Payment



Test Case: Valid Card

Description: Verify payment with valid card

Type: Sanity, Regression

Expected Result: Status 201



Test Case: Invalid Card

Description: Verify payment with invalid card

Type: Negative, Regression

Expected Result: Status 400, error returned



Edge Cases



Test Case: Invalid card numbers

Description: Test purchase or authorization with invalid card numbers

Type: Negative

Expected Result: Error returned



Test Case: Refund with wrong payment ID

Description: Attempt to refund using an invalid payment ID

Type: Negative

Expected Result: Status 404, error returned



Test Case: Authorization with invalid amounts

Description: Attempt to authorize payment with invalid or negative amount

Type: Negative

Expected Result: Status 400, error returned



Test Case: Verify flow with invalid card

Description: Attempt to verify payment with invalid card

Type: Negative

Expected Result: Status 400, error returned

