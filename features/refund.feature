Feature: Refund Payment

  @Regression
  Scenario: Full refund of a successful payment
    When I refund a payment with full amount
    Then the response status code should be 201
    And the refund status should be "SUCCEEDED"

  @Negative @Regression
  Scenario: Refund with invalid payment id
    When I refund a payment with invalid payment id
    Then the response status code should be 404
