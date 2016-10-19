*** Settings ***
Library  ../../tests/steps/LoginSteps.py
Resource  ../../resources/commons/Keywords.txt

*** Test Cases ***
Buildbot Title Displayed
    [Documentation]  Verify the Buildbot page is displayed
    [Tags]  bb  buildbot

    Set google search  Buildbot

    Click buildbot link

    Verify if buildbot title is displayed

    [Teardown]  Run Keywords  Take Screenshot If Test Fails  ${TEST NAME}

    ...         AND  Open url  www.google.com