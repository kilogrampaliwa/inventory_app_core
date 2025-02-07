import json
import os
from main_app.io.template_filler.template_filler import TemplateFiller


class TestTemplateFiller:

    @staticmethod
    def __delete_file(filename):
        """Deletes the given file in the current directory if it exists."""
        file_path = os.path.join(os.getcwd(), filename)
        if os.path.exists(file_path):
            os.remove(file_path)

    @staticmethod
    def __del_json():
        TestTemplateFiller.__delete_file("templates.json")

    @staticmethod
    def __initiation():
        templates_dict = {
            "template1": {"field1": "value1", "field2": "value2"},
            "template2": {"fieldA": "valueA", "fieldB": "valueB"}
        }
        with open("templates.json", 'w') as file:
            json.dump(templates_dict, file, indent=6)
        
        tested_object_0 = TemplateFiller("templates.json")
        tested_object_1 = TemplateFiller("templates.json", "template1")
        return tested_object_0, tested_object_1, templates_dict

    @staticmethod
    def test_init():
        try:
            tested_object_0, tested_object_1, templates_dict = TestTemplateFiller.__initiation()

            templates_0 = tested_object_0._TemplateFiller__templates
            templates_1 = tested_object_1._TemplateFiller__templates

            if templates_0 != templates_dict:
                print("templates_0 mismatch")
                TestTemplateFiller.__del_json()
                return False
            if templates_1 != templates_dict:
                print("templates_1 mismatch")
                TestTemplateFiller.__del_json()
                return False

            TestTemplateFiller.__del_json()
            return True
        except Exception as e:
            print(f"Exception in test_init: {e}")
            TestTemplateFiller.__del_json()
            return False

    @staticmethod
    def test_call_get_flattened_dict():
        try:
            tested_object, _, templates_dict = TestTemplateFiller.__initiation()
            tested_object("template1")
            expected_flattened = {"field1": "value1", "field2": "value2"}
            
            if tested_object.get_flattened_dict() != expected_flattened:
                print("Flattened dict mismatch")
                TestTemplateFiller.__del_json()
                return False
            
            TestTemplateFiller.__del_json()
            return True
        except Exception as e:
            print(f"Exception in test_call_get_flattened_dict: {e}")
            TestTemplateFiller.__del_json()
            return False

    @staticmethod
    def test_check_values_not_empty():
        try:
            tested_object, _, _ = TestTemplateFiller.__initiation()
            tested_object("template1")
            
            if not tested_object.check_values_not_empty():
                print("check_values_not_empty failed")
                return False
            
            return True
        except Exception as e:
            print(f"Exception in test_check_values_not_empty: {e}")
            return False

    @staticmethod
    def test_create_proper_dict():
        try:
            tested_object, _, _ = TestTemplateFiller.__initiation()
            tested_object("template1")
            valid_flattened_dict = {"field1": "new_value1", "field2": "new_value2"}
            
            if not tested_object.create_proper_dict(valid_flattened_dict):
                print("create_proper_dict failed")
                return False
            
            return True
        except Exception as e:
            print(f"Exception in test_create_proper_dict: {e}")
            return False

    @staticmethod
    def test_give_dict():
        try:
            tested_object, _, _ = TestTemplateFiller.__initiation()
            tested_object("template1")
            valid_flattened_dict = {"field1": "new_value1", "field2": "new_value2"}
            tested_object.create_proper_dict(valid_flattened_dict)
            
            if tested_object.give_dict() != valid_flattened_dict:
                print("give_dict output mismatch")
                return False
            
            return True
        except Exception as e:
            print(f"Exception in test_give_dict: {e}")
            return False
