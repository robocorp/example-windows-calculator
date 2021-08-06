*** Settings ***
Library           RPA.Desktop.Windows
Library           RPA.Desktop
Library           String

*** Keywords ***
Open the Calculator
    Open Executable    calc.exe    Calculator


*** Keywords ***
Add two numbers using app ids
    [Arguments]    ${first}    ${second}
    Mouse Click    id:clearEntryButton
    Mouse Click    id:num${first}Button
    Mouse Click    id:plusButton
    Mouse Click    id:num${second}Button
    Mouse Click    id:equalButton

*** Keywords ***
Read the result
    ${result}=    Get Element Rich Text    id:CalculatorResults
    ${_}    ${result}=    Split String From Right    ${result}    max_split=1
    [Return]    ${result}

*** Keywords ***
Calculate using app ids
    Open the Calculator
    Add two numbers using app ids    9    5
    ${result}=    Read the result
    Log    ${result}
    Screenshot   ids.png   overwrite=True
    RPA.Desktop.Windows.Close All Applications


*** Keywords ***
Calculate using image locators
    Open the Calculator
    Click    alias:9
    Click    alias:plus
    Click    alias:5
    Click    alias:eq
    
    ${result}=    Read the result
    Log    ${result}
    Screenshot   ids.png  overwrite=True
    RPA.Desktop.Windows.Close All Applications

*** Tasks ***
Run
    Calculate using app ids
    Calculate using image locators


