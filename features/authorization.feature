Feature: Authorization Payment

  Background:
    Given workflow is "DIRECT"

  @Sanity @Regression
  Scenario: Authorization with minimal fields
    When I authorize a payment with minimal fields
    Then the response status code should be 201
    And the authorization status should be "AUTHORIZED"

  @Regression
  Scenario: Authorization with maximal fields
    When I authorize a payment with additional data
    Then the response status code should be 201

  @Negative @Regression
  Scenario: Authorization with invalid amount
    When I authorize a payment with invalid amount
    Then the response status code should be 400
