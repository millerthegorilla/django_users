Feature: Resend confirmation page

    @locutus
    Scenario: User can resend confirmation token
        Given User is on resend confirmation page
        When User enters valid username
        And clicks on recaptcha
        And clicks on submit button
        Then an email is sent to the user's email address
        And User is able to follow email link to successfully register
        Then User is able to see registration confirmation page


    Scenario: User gets error for empty username
        Given User is on resend confirmation page
        When clicks on submit button
        Then required warning is visible


    Scenario: User gets error for incomplete captcha
        Given User is on resend confirmation page
        When User enters valid username
        And clicks on submit button
        Then captcha warning is visible
