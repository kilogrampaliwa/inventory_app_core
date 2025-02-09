import sys
import os

# Add the parent directory to sys.path (this is the root directory of your project)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Optional: Print sys.path to check if the path is added
print("sys.path:", sys.path)

# testAddTemplateList
def testAddTemplateList_test_init():
    from main_app.io.modify_template.test_add_template_list import TestAddTemplateList
    return TestAddTemplateList.test_init()
def testAddTemplateList_test_call_get_dict():
    from main_app.io.modify_template.test_add_template_list import TestAddTemplateList
    return TestAddTemplateList.test_call_get_dict()
def testAddTemplateList_test_update_check_valid():
    from main_app.io.modify_template.test_add_template_list import TestAddTemplateList
    return TestAddTemplateList.test_update_check_valid()
def testAddTemplateList_test_check_validation():
    from main_app.io.modify_template.test_add_template_list import TestAddTemplateList
    return TestAddTemplateList.test_check_validation()
def testAddTemplateList_test_save_template():
    from main_app.io.modify_template.test_add_template_list import TestAddTemplateList
    return TestAddTemplateList.test_save_template()
def testAddTemplateList_test_remove_template():
    from main_app.io.modify_template.test_add_template_list import TestAddTemplateList
    return TestAddTemplateList.test_remove_template()

# testSqliteUtils
def testSqliteUtils_test_fetch_all():
    from main_app.io.sqlite_utils.test_sqlite_utils import TestSqliteUtils
    return TestSqliteUtils.test_fetch_all()
def testSqliteUtils_test_overwrite():
    from main_app.io.sqlite_utils.test_sqlite_utils import TestSqliteUtils
    return TestSqliteUtils.test_overwrite()
def testSqliteUtils_test_save():
    from main_app.io.sqlite_utils.test_sqlite_utils import TestSqliteUtils
    return TestSqliteUtils.test_save()


# testIoModule
def testIoModule_test_take_dict():
    from main_app.io.test_io_module import TestIOmodule
    return TestIOmodule.test_take_dict()
def testIOmodule_test_add_quantity():
    from main_app.io.test_io_module import TestIOmodule
    return TestIOmodule.test_add_quantity()
def testIOmodule_test_add_to_base():
    from main_app.io.test_io_module import TestIOmodule
    return TestIOmodule.test_add_to_base()
def testIOmodule_test_delete_from_base():
    from main_app.io.test_io_module import TestIOmodule
    return TestIOmodule.test_delete_from_base()
def testIOmodule_test_remove_template():
    from main_app.io.test_io_module import TestIOmodule
    return TestIOmodule.test_remove_template()
def testIOmodule_test_subtract_quantity():
    from main_app.io.test_io_module import TestIOmodule
    return TestIOmodule.test_subtract_quantity()





