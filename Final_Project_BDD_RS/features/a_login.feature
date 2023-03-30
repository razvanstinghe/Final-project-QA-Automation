Feature: SWAG LABS Login

  Background:
    Given I am on the home page

    @smoke
  Scenario Outline: Sign in with INVALID credentials

    When I click and type-in invalid username "<username>"
    And I click and type-in invalid password "<password>"
    And I click on the LOGIN button with wrong credentials
    Then I check the error message:Epic sadface: Username and password do not match any user in this service

    Examples:
      | username      | password     |
      | user          | sauce        |

    @smoke
  Scenario: Sign in with no username and no password

    When I leave the username field empty
    And I leave the password field empty
    And I click on the LOGIN button with the empty credentials
    Then I check the error message: Epic sadface: Username is required

    @smoke
  Scenario: Sign in with VALID credentials

    When I type in a valid username
    And I type in a valid password
    And I click on the LOGIN button with the valid credentials
    Then I check the confirmation message: Products



