Feature: Purchase Payment

  Background:
    Given workflow is "DIRECT"
    And valid authentication headers are prepared

  @Sanity @Regression @Integration
  Scenario: Purchase payment with minimal fields
    When I create a purchase payment with minimal fields
    Then the response status code should be 201
    And the payment status should be "SUCCEEDED"

  @Regression @Integration
  Scenario: Purchase payment with maximal fields
    When I create a purchase payment with customer_payer and additional_data
    Then the response status code should be 201
    And customer details should be present in the response

  @Negative @Regression
  Scenario: Purchase payment with invalid card number
    When I create a purchase payment with invalid card number
    Then the response status code should be 400
    And an error message should be returned
