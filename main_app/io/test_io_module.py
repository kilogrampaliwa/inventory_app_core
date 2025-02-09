import os
import json
from main_app.io.io_module import IOmodue


class TestIOmodule:

    def __delete_file(filename):
        file_path = os.path.join(os.getcwd(), filename)
        if os.path.exists(file_path):
            os.remove(file_path)

    def __del_jsons():
        TestIOmodule.__delete_file("inventory_templates_mandatory.json")
        TestIOmodule.__delete_file("inventory_templates.json")

    def __initiation():
        mandatory_dict = {"name": "name", "quantity": "quantity", "measurement": "measurement", "vat": "vat", "qr_code": "qr_code"}
        additional_dict = {"name": "extra_name", "quantity": "quantity", "measurement": "measurement", "vat": "vat", "qr_code": "qr_code", "extra": "extra"}
        with open("inventory_templates_mandatory.json", 'w') as file:
            json.dump(mandatory_dict, file, indent=6)
        with open("inventory_templates.json", 'w') as file:
            json.dump([additional_dict], file, indent=6)
        
        tested_object = IOmodue(os.getcwd())
        return tested_object, mandatory_dict, additional_dict

    def test_take_dict():
        try:
            tested_object, _, _ = TestIOmodule.__initiation()
            if not isinstance(tested_object.take_dict("templates"), list):
                print("take_dict failed for templates")
                return False
            return True
        except Exception as e:
            print(f"Exception in test_take_dict: {e}")
            return False

    def test_add_to_base():
        try:
            tested_object, _, additional_dict = TestIOmodule.__initiation()
            tested_object.add_to_base("templates", additional_dict, "extra_name")
            if not any(t["name"] == "extra_name" for t in tested_object.take_dict("templates")):
                print("add_to_base failed")
                return False
            return True
        except Exception as e:
            print(f"Exception in test_add_to_base: {e}")
            return False

    def test_subtract_quantity():
        try:
            tested_object, _, _ = TestIOmodule.__initiation()
            tested_object.add_to_base("current", {"name": "item1", "quantity": 10})
            tested_object.substract_quantity("current", "item1", 5)
            result = tested_object.take_dict("current")
            for item in result:
                if item["name"] == "item1" and item["quantity"] != 5:
                    print("substract_quantity failed")
                    return False
            return True
        except Exception as e:
            print(f"Exception in test_subtract_quantity: {e}")
            return False

    def test_add_quantity():
        try:
            tested_object, _, _ = TestIOmodule.__initiation()
            tested_object.add_to_base("current", {"name": "item1", "quantity": 5})
            tested_object.add_quantity("current", "item1", 5)
            result = tested_object.take_dict("current")
            for item in result:
                if item["name"] == "item1" and item["quantity"] != 10:
                    print("add_quantity failed")
                    return False
            return True
        except Exception as e:
            print(f"Exception in test_add_quantity: {e}")
            return False

    def test_remove_template():
        try:
            tested_object, _, additional_dict = TestIOmodule.__initiation()
            tested_object.remove_template("extra_name")
            if any(t["name"] == "extra_name" for t in tested_object.take_dict("templates")):
                print("remove_template failed")
                return False
            return True
        except Exception as e:
            print(f"Exception in test_remove_template: {e}")
            return False

    def test_delete_from_base():
        try:
            tested_object, _, _ = TestIOmodule.__initiation()
            tested_object.add_to_base("current", {"name": "item1", "quantity": 5})
            tested_object.delete_from_base("current", "item1")
            result = tested_object.take_dict("current")
            if any(item["name"] == "item1" for item in result):
                print("delete_from_base failed")
                return False
            return True
        except Exception as e:
            print(f"Exception in test_delete_from_base: {e}")
            return False
