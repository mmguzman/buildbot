*** Settings ***
Library  ../../tests/steps/LoginSteps.py
Resource  ../../resources/commons/Keywords.txt

*** Test Cases ***
Robot Framework Title Displayed
    [Documentation]  Verify the Robot Frameowork page is displayed
    [Tags]  rf  robot  buildbot

    Set google search  Robot Framework

    Click robot framework link

    Verify if robot framework title is displayed

    [Teardown]  Run Keywords  Take Screenshot If Test Fails  ${TEST NAME}

    ...         AND  Open url  www.google.com