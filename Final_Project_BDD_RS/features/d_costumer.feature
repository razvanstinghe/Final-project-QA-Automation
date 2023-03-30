Feature: SWAG LABS Costumer details - Your Information


  Background:
    Given I am on the costumer details page

  @smoke
  Scenario: Empty First Name, Last Name and Zip-Postal Code fields


    When I leave the First Name1 field empty
    And I leave the Last Name1 field empty
    And I leave the Zip-Postal Code1 field empty
    And I press the Continue button_1
    Then I check the confirmation message_1: Error: First Name is required

#    When I leave the First Name field empty
#    And I leave the Last Name field empty
#    And I leave the Zip-Postal Code field empty
#    And I press the Continue button_2
#    Then I check the confirmation message_2: Error: Last Name is required
#
#    When I leave the First Name field empty
#    And I leave the Last Name field empty
#    And I leave the Zip-Postal Code field empty
#    And I press the Continue button_3
#    Then I check the confirmation message_3: Error: Postal Code is required
#
#
#    When I fill-in the First Name, in digits
#    And I fill-in the Last Name, in digits
#    And I fill-in the Zip-Postal code, in letters
#    And I press the Continue button_4
#    Then I check the confirmation message_4: Checkout: Overview
#
#
#    When I fill-in the First Name, in letters
#    And I fill-in the Last Name, in letters
#    And I fill-in the Zip-Postal code, in digits
#    And I press the Continue button_5
#    Then I check the confirmation message_5: Checkout: Overview
#
#      Examples:
#
#      |First_Name     |Last_Name     |Zip_Postal_Code |
#      |None           |None          |None            |
#      |Razvan         |None          |None            |
#      |Razvan         |Stinghe       |None            |
#      |123456         |654321        |abcde           |
#      |Razvan         |Stinghe       |123456          |



  @smoke
  Scenario: Empty Last Name and Zip-Postal Code fields


    When I fill-in the First Name2 field, in letters
    And I leave the Last Name2 field empty
    And I leave the Zip-Postal Code2 field empty
    And I press the Continue button_2
    Then I check the confirmation message_2: Error: Last Name is required

  @smoke
  Scenario: Empty Zip-Postal Code field


    When I fill-in the First Name3 field, in letters
    And I fill-in the Last Name3 field, in letters
    And I leave the Zip-Postal Code3 field empty
    And I press the Continue button_3
    Then I check the confirmation message_3: Error: Postal Code is required


  @smoke
  Scenario: Fill in unacceptable costumer details


    When I fill-in the First Name4, in digits
    And I fill-in the Last Name4, in digits
    And I fill-in the Zip-Postal Code4, in letters
    And I press the Continue button_4
    Then I check the confirmation message_4: Checkout: Overview


  @smoke
  Scenario: Fill in acceptable costumer details


    When I fill-in the First Name5, in letters
    And I fill-in the Last Name5, in letters
    And I fill-in the Zip-Postal Code5, in digits
    And I press the Continue button_5
    Then I check the confirmation message_5: Checkout: Overview