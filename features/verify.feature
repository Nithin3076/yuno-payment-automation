Feature: Verify Card Payment

  @Sanity @Regression
  Scenario: Verify payment with valid card
    When I create a payment with verify enabled
    Then the response status code should be 201

  @Negative @Regression
  Scenario: Verify payment with invalid card
    When I create a payment with verify enabled using invalid card
    Then the response status code should be 400
