import json
import os
from main_app.io.modify_template import add_template_list





class TestAddTemplateList:


    @staticmethod
    def __delete_file(filename):
        """Deletes the given file in the current directory if it exists."""
        file_path = os.path.join(os.getcwd(), filename)  # Get full path in the current directory

        if os.path.exists(file_path):
            os.remove(file_path)


    @staticmethod
    def __del_jsons():
        TestAddTemplateList.__delete_file("mandatory.json")
        TestAddTemplateList.__delete_file("current.json"  )


    @staticmethod
    def __initiation():
            mandatory_dict = {"name": "name","quantity":"quantity","measuremant":"measurement","vat":"vat","qr_code": "qr_code"}
            additiona_dict = {"name": "extra_name","quantity":"quantity","measuremant":"measurement","vat":"vat","qr_code": "qr_code","extra": "extra"}
            with open("mandatory.json", 'w') as file:   json.dump(mandatory_dict, file, indent = 6)
            with open("current.json"  , 'w') as file:   json.dump([additiona_dict], file, indent = 6)
            tested_object_0 = add_template_list.AddTemplateList("mandatory.json", "current.json")
            tested_object_1 = add_template_list.AddTemplateList("mandatory.json", "current.json", "extra_name")
            return tested_object_0, tested_object_1, mandatory_dict, additiona_dict



    @staticmethod
    def test_init():
        try:

            #  case initiation
            #----------------------------------------------------------

            tested_object_0, tested_object_1, mandatory_dict, additiona_dict = TestAddTemplateList.__initiation()

            mandatory_0 = tested_object_0._AddTemplateList__mandatory
            templates_0 = tested_object_0._AddTemplateList__templates

            mandatory_1 = tested_object_1._AddTemplateList__mandatory
            templates_1 = tested_object_1._AddTemplateList__templates

            #----------------------------------------------------------

            if mandatory_0 != mandatory_dict:
                print("mandatory_0")
                TestAddTemplateList.__del_jsons()
                return False
            if templates_0 != [additiona_dict]:
                print("templates_0")
                TestAddTemplateList.__del_jsons()
                return False
            if mandatory_1 != additiona_dict:
                print("mandatory_1")
                TestAddTemplateList.__del_jsons()
                return False
            if templates_1 != [additiona_dict]:
                print("templates_1")
                TestAddTemplateList.__del_jsons()
                return False
            TestAddTemplateList.__del_jsons()

            return True

        except Exception as e:
            print(f"except {e}")
            TestAddTemplateList.__del_jsons()
            return False


    @staticmethod
    def test_call_get_dict():
        try:

            #  case initiation
            #----------------------------------------------------------

            tested_object_0, tested_object_1, mandatory_dict, additiona_dict = TestAddTemplateList.__initiation()
            tested_object_2, tested_object_3, mandatory_dict, additiona_dict = TestAddTemplateList.__initiation()

            tested_object_0()
            tested_object_1()
            tested_object_2(initial_dict_name="extra_name")
            tested_object_3(initial_dict_name="extra_name")
            #----------------------------------------------------------

            if   tested_object_0.get_dict() != mandatory_dict:
                print("dict_0")
                TestAddTemplateList.__del_jsons()
                return False
            elif tested_object_1.get_dict() != additiona_dict:
                print("dict_1")
                TestAddTemplateList.__del_jsons()
                return False
            elif tested_object_2.get_dict() != additiona_dict:
                print("dict_2")
                TestAddTemplateList.__del_jsons()
                return False
            elif tested_object_3.get_dict() != additiona_dict:
                print("dict_3")
                TestAddTemplateList.__del_jsons()
                return False
            TestAddTemplateList.__del_jsons()

            return True

        except Exception as e:
            print(f"except {e}")
            TestAddTemplateList.__del_jsons()
            return False



    @staticmethod
    def test_update_check_valid():
        try:
            tested_object, _, _, additiona_dict = TestAddTemplateList.__initiation()
            
            valid_update = {"name": "valid_name", "quantity": "10", "measuremant": "kg", "vat": "20", "qr_code": "12345"}
            invalid_update = {"name": "invalid_name", "missing_field": "oops"}

            if not tested_object.update_check_valid(valid_update):
                print("update_check_valid failed for valid update")
                return False
            if tested_object.update_check_valid(invalid_update):
                print("update_check_valid passed for invalid update")
                return False

            return True
        except Exception as e:
            print(f"Exception in test_update_check_valid: {e}")
            return False

    @staticmethod
    def test_check_validation():
        try:
            tested_object, _, _, _ = TestAddTemplateList.__initiation()
            valid_update = {"name": "valid_name", "quantity": "10", "measuremant": "kg", "vat": "20", "qr_code": "12345"}
            
            tested_object.update_check_valid(valid_update)
            if not tested_object.check_validation():
                print("check_validation failed after valid update")
                return False
            
            return True
        except Exception as e:
            print(f"Exception in test_check_validation: {e}")
            return False

    @staticmethod
    def test_save_template():
        try:
            tested_object, _, _, _ = TestAddTemplateList.__initiation()
            valid_update = {"name": "valid_name", "quantity": "10", "measuremant": "kg", "vat": "20", "qr_code": "12345"}
            
            tested_object.update_check_valid(valid_update)
            if not tested_object.save_template():
                print("save_template failed when it should succeed")
                return False
            
            return True
        except Exception as e:
            print(f"Exception in test_save_template: {e}")
            return False

    @staticmethod
    def test_remove_template():
        try:
            tested_object, _, _, additiona_dict = TestAddTemplateList.__initiation()
            template_name = additiona_dict["name"]
            
            tested_object.remove_template(template_name)
            if any(t["name"] == template_name for t in tested_object._AddTemplateList__templates):
                print("remove_template failed")
                return False
            
            return True
        except Exception as e:
            print(f"Exception in test_remove_template: {e}")
            return False



