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
        Then User is able to see registration confirmation page
        And an email is sent to the user's email address
##
    #Scenario: User can visit the resend confirmation page
        #Given User is on registration page
        #When User clicks "resend confirmation link"
        #Then User is taken to "resend confirmation page"
