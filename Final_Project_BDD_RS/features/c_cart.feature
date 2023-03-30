Feature: SWAG LABS Shopping cart - Your Cart


  Background:
    Given I am on the shopping cart page

  @smoke
  Scenario: Shopping cart

    When I press the Remove button for the 5th item-Sauce Labs Fleece Jacket
    And I press the Checkout button
    Then I check the confirmation message: Checkout: Your Information