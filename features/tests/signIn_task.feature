Feature:Test for signIn functionality

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open target main page
    When click signin icon
    When Click on Signin button on navigation menu
    Then Verify Sign in or create account form opened
