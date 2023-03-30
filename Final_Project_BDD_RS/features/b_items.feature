Feature: SWAG LABS Choosing items - Products Page


  Background:

    Given I am on the buying page

   @smoke
  Scenario: Filter items from Z to A

    When I press the filter drop-down list
    And I select filtration from Z to A
    Then I check if item Test.allTheThings() T-Shirt (Red) is the 1st item

   @smoke
  Scenario: Filter items from A to Z

    When I press again the filter drop-down list
    And I select filtration from A to Z
    Then I check if item Sauce Labs Backpack is the 1st item

   @smoke
  Scenario: Choosing items to buy

    When I press Add to cart button for the 1st item-Sauce Labs Backpack
    And I press Add to cart button for the 2nd item-Sauce Labs Bolt T-Shirt
    And I press Add to cart button for the 4th item-Sauce Labs Bike Light
    And I press the Remove button for the 2nd item-Sauce Labs Bolt T-Shirt
    And I press Add to cart button for the 5th item-Sauce Labs Fleece Jacket
    And I press the Cart button
    Then I check the confirmation message: Your Cart

