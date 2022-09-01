Feature: Reset password page

    Scenario: User can reset password
        Given User is on reset password page
        When User enters valid email address
        And clicks on recaptcha
        And clicks on submit button
        Then User is able to see password done page
        And User is sent password reset email
        And User can follow link
        And User can view password reset confirm page
        And User can enter password twice
        And clicks on submit button
        And User can see password reset complete page

    Scenario: User gets error for empty username
        Given User is on reset password page
        When clicks on submit button
        Then required warning is visible


    Scenario: User gets error for incomplete captcha
        Given User is on reset password page
        When User enters valid email address
        And clicks on submit button
        Then required warning is visible