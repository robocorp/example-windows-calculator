*** Settings ***
Library           String
Library           RPA.Windows             WITH NAME    Win
Library           RPA.Desktop             WITH NAME    Desk
Task Teardown     Close Current Window

*** Keywords ***
Open the Calculator
    Desk.Open Application    calc.exe 
    Win.Foreground Window    Calculator

Add two numbers using app ids
    [Arguments]    ${first}    ${second}
    Win.Click    id:clearEntryButton
    Win.Click    id:num${first}Button
    Win.Click    id:plusButton
    Win.Click    id:num${second}Button
    Win.Click    id:equalButton

Log the result
    ${result}=    Get Attribute    id:CalculatorResults    Name
    Log    ${result}

Calculate using app ids
    Open the Calculator
    Add two numbers using app ids    9    5
    Log the result
    Win.Screenshot    Calculator   ids.png

Calculate using image locators
    Open the Calculator
    Desk.Click    alias:9
    Desk.Click    alias:plus
    Desk.Click    alias:5
    Desk.Click    alias:eq

    Log the result
    Win.Screenshot    Calculator   images.png

*** Tasks ***
Run Examples
    Calculate using app ids
    Calculate using image locators