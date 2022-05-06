*** Settings ***
Library           String
Library           RPA.Windows
Task Teardown     Close Window     name:Calculator

*** Keywords ***
Open the Calculator
    Windows Search    Calculator
    #Foreground Window    Calculator

Add two numbers using app ids
    [Arguments]    ${first}    ${second}
    Click    id:clearEntryButton
    Click    id:num${first}Button
    Click    id:plusButton
    Click    id:num${second}Button
    Click    id:equalButton

Log results
    ${result}=    Get Attribute    id:CalculatorResults    Name
    Log    ${result}
    Screenshot    Calculator   %{ROBOT_ARTIFACTS}${/}id-based-result.png

Calculate using app ids
    Open the Calculator
    Add two numbers using app ids    9    5
    Log results

*** Tasks ***
Run Example
    Calculate using app ids