

from main_app import io as __io
from pathlib import Path as __Path


class MainAplication:

    def __init__(common):

        common.__PATH_CLASS = __Path.cwd()
        common.__io_module = __io.IOmodue(common.__PATH_CLASS)

    #-----------------------------------------------------------------------------------------------
    #-------------------------------------------TEMPLATES-------------------------------------------
    #-----------------------------------------------------------------------------------------------

    def templateListNames(common):

        template_dicts = common.__io_module.take_names_quantities("templates")
        template_list = []
        for x in template_dicts: template_list.append(x["templates"])
        return template_list

    def templateListDicts(common): return common.__io_module.take_dict("templates")

    def templateAdd(common, name: str, structure: dict, base_name: str):

        try:
            common.__io_module.add_template_list(name, base_name)
            common.__io_module.add_template_list.update_check_valid(structure)
            common.__io_module.add_template_list.check_validation()
            common.__io_module.add_template_list.save_template()
        except ValueError as e: raise ValueError(f"MainApplication templateAdd: {e}")

    def templateRemove(common, name: str):

        try:
            common.__io_module.add_template_list.remove_template(name)
        except ValueError as e: raise ValueError(f"MainApplication templateRemove: {e}")

    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------ADD ELEMENTS------------------------------------------
    #-----------------------------------------------------------------------------------------------

    def addElementExistingData(common):                             return  common.__io_module.take_dict("current")

    def addElementExistingNamesQuantities(common):                  return  common.__io_module.take_names_quantities("current")

    def addElementExistingAddQuantity(common, name: str, quantity: int):    common.__io_module.add_quantity("current", name, quantity)

    def addElementNew(common, name: str, dict_data: str):                   common.__io_module.add_to_base("current", dict_data, name)

    def addElementSubstract(common, name:str, quantity: int):               common.__io_module.substract_quantity("current", name, quantity)

    def addElementDelete(common, name: str):                                common.__io_module.delete_from_base("current", name)

    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------SELL ELEMENT------------------------------------------
    #-----------------------------------------------------------------------------------------------

    def sellElement(common, name: str, quantity: int):

        common.addElementSubstract(name, quantity)
        names_and_quantities = common.__io_module.take_names_quantities("unsettled")
        new_flag = True
        for x in names_and_quantities:
            if x["name"] == name:
                common.__io_module.add_quantity("unsettled", name, quantity)
                new_flag = False
        if new_flag:
            current_dict_list = common.addElementExistingData()
            for x in current_dict_list:
                if x["name"]==name:
                    common.__io_module.add_to_base(name, x)

    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------CREATE INVOICE----------------------------------------
    #-----------------------------------------------------------------------------------------------

    # ----- invoice creation to be done