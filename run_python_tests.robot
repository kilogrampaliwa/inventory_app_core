*** Settings ***
Library    C:\inventory_app\inventory_app_core\main_app\io\modify_template\test_add_template_list.py
*** Variables ***
${PYTHON_EXEC}    python   # Use 'python3' if needed
${PYTHON_TEST_SCRIPT}    C:\inventory_app\inventory_app_core\main_app\io\modify_template\test_add_template_list.py  # Replace with the path to your pytest file

*** Test Cases ***
Run Pytest Tests
    Run Process    ${PYTHON_EXEC}    -m    pytest    ${PYTHON_TEST_SCRIPT}  

