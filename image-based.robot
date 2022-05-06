*** Settings ***
Library           String
Library           RPA.Windows
Library           RPA.Desktop
Task Teardown     Close Window     name:Calculator

*** Keywords ***
Open the Calculator
    Open Application    calc.exe

Log the result
    ${result}=    Get Attribute    id:CalculatorResults    Name
    Log    ${result}

Calculate using image locators
    [Documentation]  The locators expect the calculator to be Windows 10 calculator in white theme.
    ...              So the automation will fail 
    Open the Calculator

    TRY
        RPA.Desktop.Click    alias:9
        RPA.Desktop.Click    alias:plus
        RPA.Desktop.Click    alias:5
        RPA.Desktop.Click    alias:eq
        Log the result
    EXCEPT
        Log   The image locators expect the calculator to be Windows 10 calculator in white theme.  level=ERROR
    FINALLY
        Screenshot    Calculator   %{ROBOT_ARTIFACTS}${/}image-based-result.png  
    END

*** Tasks ***
Run Example
    Calculate using image locators