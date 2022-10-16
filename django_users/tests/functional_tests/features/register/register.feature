Feature: Registration page


    Scenario: Visiting the registration page
        Given User is on registration page
        Then I should see the username input
        And I should see the password input
        And I should see the password confirmation input
        And I should see the recaptcha
        And I should see the resend confirmation link
        And I should see a submit button


    Scenario: Register to use application
        Given User is on registration page
        When User completes valid details
        And clicks on recaptcha
        And clicks on submit button
        Then an email is sent to the user's email address
        And User is able to follow email link to successfully register
        And User is able to see registration confirmation page


    Scenario: App fails to register invalid token
        Given User opens invalid link
        Then error is shown in template


    Scenario: User can visit the resend confirmation page
        Given User is on registration page
        When User clicks resend confirmation link
        Then User is taken to resend confirmation page

    Scenario: User gets error for empty username
        Given User is on registration page
        When clicks on submit button
        Then required warning is visible


    Scenario: User gets error for empty email
        Given User is on registration page
        When User enters valid username
        And clicks on submit button
        Then required warning is visible


    Scenario: User gets error for incomplete password1
        Given User is on registration page
        When User enters valid username
        And User enters valid email address
        And clicks on submit button
        Then required warning is visible


    Scenario: User gets error for incomplete password2
        Given User is on registration page
        When User enters valid username
        And User enters valid email address
        And User enters valid password1
        And clicks on submit button
        Then required warning is visible


    Scenario: User gets error for incomplete captcha
        Given User is on registration page
        When User enters valid username
        And User enters valid email address
        And User enters valid password1
        And User enters valid password2
        And clicks on submit button
        Then captcha warning is visible


    Scenario: User email is validated correctly
        Given User is on registration page
        When User enters valid username
        And User enters valid password1
        And User enters valid password2
        And User enters incorrect email address
        And clicks on submit button
        Then invalid email message is visible