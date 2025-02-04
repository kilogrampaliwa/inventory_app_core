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
    def init():
        try:
            mandatory_dict = {"name": "name","quantity":"quantity","measuremant":"measurement","vat":"vat","qr_code": "qr_code"}
            additiona_dict = {"name": "extra_name","quantity":"quantity","measuremant":"measurement","vat":"vat","qr_code": "qr_code","extra": "extra"}
            with open("mandatory.json", 'w') as file:   json.dump(mandatory_dict, file, indent = 6)
            with open("current.json"  , 'w') as file:   json.dump([additiona_dict], file, indent = 6)
            tested_object_0 = add_template_list.AddTemplateList("mandatory.json", "current.json")
            tested_object_1 = add_template_list.AddTemplateList("mandatory.json", "current.json", "extra_name")

            mandatory_0 = tested_object_0._AddTemplateList__mandatory
            templates_0 = tested_object_0._AddTemplateList__templates
            modifier_0  = tested_object_0._AddTemplateList__modifier

            mandatory_1 = tested_object_1._AddTemplateList__mandatory
            templates_1 = tested_object_1._AddTemplateList__templates
            modifier_1  = tested_object_1._AddTemplateList__modifier

            true_flag = True

            if mandatory_0 != mandatory_dict:
                print("mandatory_0")
                TestAddTemplateList.__del_jsons()
                return False
            if templates_0 != additiona_dict:
                print("templates_0")
                TestAddTemplateList.__del_jsons()
                return False
            if mandatory_1 != mandatory_dict:
                print("mandatory_1")
                TestAddTemplateList.__del_jsons()
                return False
            if templates_1 != additiona_dict:
                print("templates_1")
                TestAddTemplateList.__del_jsons()
                return False
            TestAddTemplateList.__del_jsons()

            return True

        except Exception as e:
            print(f"except {e}")
            TestAddTemplateList.__del_jsons()
            return False










