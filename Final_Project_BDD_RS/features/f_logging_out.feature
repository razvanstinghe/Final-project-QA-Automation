Feature: SWAG LABS Logging out from the page


  Background:
    Given I am on the order confirmation page

  @smoke
  Scenario: Logging out

    When I check the message Checkout: Complete!
    And I click on the left top corner menu(3 horizontal stripes)
    And I click the logout button
    Then I check the logout confirmation - Accepted usernames are: