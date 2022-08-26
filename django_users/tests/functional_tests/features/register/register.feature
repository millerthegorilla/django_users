Feature: Registration page

    Scenario: Visiting the registration page
        Given User is on registration page
        Then I should see the username input
        And I should see the password input
        And I should see the password confirmation input
        And I should see the recaptcha
        And I should see the resend confirmation link
        And I should see a submit button

    @locutus
    @flaky("django_email_verification thread flakes when run with other tests, solution is to run this feature on its own.")
    Scenario: Register to use application
        Given User is on registration page
        When User completes valid details
        And clicks on recaptcha
        And clicks on submit button
        Then an email is sent to the user's email address
        And User is able to follow link to successfully register
        And User is able to see registration confirmation page
##
    #Scenario: User can visit the resend confirmation page
        #Given User is on registration page
        #When User clicks "resend confirmation link"
        #Then User is taken to "resend confirmation page"
