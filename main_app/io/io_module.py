from main_app.io.modify_template import *
from main_app.io.sqlite_utils import *
from main_app.io.template_filler import *
from main_app.utils.json_utils import *

class IOmodue:

    def __int__(self, database_path:str):

        self.__current_inventory = SqliteUtils(database_path+"/inventory/current_inventory.db")
        self.__history_inventory = SqliteUtils(database_path+"/inventory/history_inventory.db")

        self.add_template_list = AddTemplateList(database_path+"/inventory/inventory_templates_mandatory.json", database_path+"/inventory/inventory_templates.json")
        self.__fill_template = TemplateFiller(database_path+"/inventory/inventory_templates.json")

    def take_dict(self, database_name:str)->list|dict:

        if   database_name=="current":      return self.__current_inventory.fetch_all()
        elif database_name=="history":      return self.__history_inventory.fetch_all()
        elif database_name=="templates":    return self.__fill_template.get_flattened_whole_dict()
        else: raise ValueError("IOmodule: Database not achievable.")

    def __save_base(self, database_name:str, new_list_data: list, item_name:str = "none")->bool:

        if   item_name=="none" and new_list_data==[]: raise ValueError("IOmodule: no new data given.")
        elif item_name!="none" and new_list_data!=[]: raise ValueError("IOmodule: Too much data given.")
        elif item_name=="none":
            if database_name in ["templates"]:  raise ValueError("IOmodule: item_name not provided")
            elif database_name=="current":
                try:
                    self.__current_inventory.overwrite(new_list_data)
                    return True
                except ValueError as e: raise ValueError(f"IOmodule: {e}")
                except: raise ValueError("IOmodue: issue in savig database")
                return False
            elif database_name=="history":
                try:
                    self.__history_inventory.overwrite(new_list_data)
                    return True
                except ValueError as e: raise ValueError(f"IOmodule: {e}")
                except: raise ValueError("IOmodue: issue in savig database")
                return False
        else:
            if database_name in ["current", "history"]:  raise ValueError("IOmodule: Wrong data type.")
            elif database_name=="templates":
                try:
                    self.__fill_template(item_name)
                    self.__fill_template.check_values_not_empty()
                    inventory = self.take_dict("current")
                    inventory.append(self.__fill_template.give_dict(new_list_data[0]))
                    self.__save_base("current", inventory)
                    return True
                except ValueError as e: raise ValueError(f"IOmodule: {e}")
                except: raise ValueError("IOmodue: issue in savig database")
                return False

    def add_to_base(self, database_name:str, new_dict_data: dict, item_name:str = "none")->bool:


        if database_name in ["current", "history"]:
            modified_dict_list = self.take_dict(database_name)
            modified_dict_list.append(new_dict_data)
            self.__save_base(database_name, modified_dict_list)
        elif database_name in ["templates"]:
            self.__save_base(database_name, [new_dict_data], item_name)

    def take_names_quantities(self, database_name:str, item_names: list) -> list:

        database_list = self.take_dict(database_name)
        out_list = []

        for item_name in item_names:
            for row in database_list:
                if row["name"]==item_name:
                    out_list.append({"name":row["name"], "quantity":row["quantity"]})
        return out_list

    def __modify_quantity(self, database_name:str, item_name:str, add_true_sub_false:bool, quantity_change:int=1)->bool:

        database_list = self.take_dict(database_name)

        for row in database_list:
            if row["name"]==item_name:
                if add_true_sub_false:  row["quantity"]+=quantity_change
                else:                   row["quantity"]-=quantity_change
                if row["quantity"]<=0:
                    database_list.remove(row)
        self.__save_base(database_name, database_list)

        return True

    def substract_quantity(self, database_name:str, item_name:str, quantity_to_substract:int=1) -> bool:

        return self.__modify_quantity(database_name, item_name, False, quantity_to_substract)

    def add_quantity(self, database_name:str, item_name:str, quantity_to_add:int=1) -> bool:

        return self.__modify_quantity(database_name, item_name, True, quantity_to_add)

    def remove_template(self, item_name:str):

        self.add_template_list.remove_template(item_name)