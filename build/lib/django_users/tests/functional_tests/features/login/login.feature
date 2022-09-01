# TODO create class that is passed the user is on login page step for all functions
# Also create paramaterised step in which link/button etc is passed as parameter
# learn about pytest logging

Feature: Login page

    Scenario: Visiting the login page
        Given User is on login page
        Then I should see the username input
        And I should see the password input
        And I should see the registration link
        And I should see the reset password link
        And I should see a submit button

    Scenario: Login to Application
        Given User is on login page
        When User fills valid username and password
        And clicks on submit button
        Then User is able to login and view landing page

    Scenario: User can visit the registration page
        Given User is on login page
        When User clicks "registration" link
        Then User is taken to "registration" page
    
    Scenario: User can visit the reset password page
        Given User is on login page 
        When User clicks "reset_password" link
        Then User is taken to "reset_password" page
