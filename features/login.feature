Feature: Regression Pack for Login Module


  @regression
    Scenario: Verify whether the user can log in successfully with valid username and password
      Given I login with username
      Then Validate the tilte text

#  @regression
#    Scenario: Verify whether the system displays an error message for invalid username
#      Given the user is on login page
#      When the user enters an invalid username
#      Then the user clicks on the Login button
#      Then the system should display an error message for invalid username
#
#
#  @regression
#    Scenario: Verify whether the system displays an error message for invalid username and valid password for keycloak
#      Given the user is on login page
#      When the user enters an invalid username in keycloak
#      Then the system should display an error message for invalid username on keycloak page
#
#
#  @regression
#    Scenario: Verify whether the system displays an error message for username and invalid password for keycloak
#      Given the user is on login page
#      When the user enters an valid username and invalid password in keycloak
#      Then the system should display an error message for valid username and invalid password on keycloak page