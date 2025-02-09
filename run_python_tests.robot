*** Settings ***
Library    test_functions_for_robot.py

*** Test Cases ***
AddTemplateList Test Init
    ${result}=      testAddTemplateList_test_init
    Should Be True    ${result}
AddTemplateList Call Get Dict
    ${result}=      testAddTemplateList_test_call_get_dict
    Should Be True    ${result}
AddTemplateList Update Check Valid
    ${result}=      testAddTemplateList_test_update_check_valid
    Should Be True    ${result}
AddTemplateList Check Validation
    ${result}=      testAddTemplateList_test_check_validation
    Should Be True    ${result}
AddTemplateList Save Template
    ${result}=      testAddTemplateList_test_save_template
    Should Be True    ${result}
AddTemplateList Remove Template
    ${result}=      testAddTemplateList_test_remove_template
    Should Be True    ${result}


