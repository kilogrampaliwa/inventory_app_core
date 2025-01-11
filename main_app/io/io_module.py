from main_app.io.add_template import *
from main_app.io.sqlite_utils import *
from main_app.io.template_filler import *
from main_app.utils.json_utils import *

class IOmodue:

    def __int__(self, database_path:str):

        self.__current_inventory = SqliteUtils(database_path+"/inventory/current_inventory.db")
        self.__history_inventory = SqliteUtils(database_path+"/inventory/history_inventory.db")

        self.__inventory_templates_path = database_path+"/inventory/inventory_templates.json"

        self.add_template = AddTemplate(database_path+"/inventory/inventory_templates_mandatory.json", database_path+"/inventory/inventory_templates.json")
        self.__fill_template = TemplateFiller(database_path+"/inventory/inventory_templates.json")

    def take_dict(self, database_name:str)->list:

        if   database_name=="current": self.__current_inventory.fetch_all()
        elif database_name=="history": self.__history_inventory.fetch_all()
        elif database_name=="templates": self.__fill_template.get_flattened_whole_dict()

