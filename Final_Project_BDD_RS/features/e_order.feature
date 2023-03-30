Feature: SWAG LABS Finishing order page - Overview


  Background:
    Given I am on the order page

  @smoke
  Scenario: Order page

    When I check the item1 existence in the cart
    And I check the item4 existence in the cart
    And I press the Finish button
    Then I check the confirmation message: Checkout: Complete!