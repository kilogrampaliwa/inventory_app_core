from main_app.io.modify_template.modify_to_dict import ModifyInsides
from main_app.utils import load_json, save_json, plain_dict


class AddTemplateList:
    def __init__(self, mandatory_dict_path: str, templates_dict_path: str, initial_dict_name: str = "none"):
        """
        Initializes the AddTemplate object.

        Args:
            new_name (str): The name of the new template to be added.
            mandatory_dict_path (str): Path to the JSON file containing mandatory fields.
            templates_dict_path (str): Path to the JSON file containing existing templates.
            initial_dict_name (str, optional): The name of an existing dictionary to initialize mandatory fields. 
                                               Defaults to "none".

        Raises:
            ValueError: If the provided initial_dict_name does not exist in the templates.
        """
        self.__name = False
        self.__templates_dict_path = templates_dict_path

        self.__mandatory = load_json(mandatory_dict_path)
        self.__templates = load_json(templates_dict_path)
        self.__validation = False

        if initial_dict_name != "none":
            if plain_dict(initial_dict_name, self.__templates):
                for row in self.__templates:
                    if row["name"]== initial_dict_name:
                        self.__mandatory = row
            else:
                raise ValueError("AddTemplate: initial_dict_name doesn't exist.")

        self.__modifier = ModifyInsides(self.__mandatory)


    def __call__(self, name:str = "none", initial_dict_name: str = "none"):

        if initial_dict_name != "none":
            if plain_dict(initial_dict_name):
                self.__mandatory = self.__templates[initial_dict_name]
            else:
                raise ValueError("AddTemplate: initial_dict_name doesn't exist.")

        if name != "none":
            self.__name = name

        self.__modifier = ModifyInsides(self.__mandatory)


    def get_dict(self) -> dict:
        """
        Retrieves the current state of the mandatory dictionary.

        Returns:
            dict: The current dictionary managed by ModifyInsides.
        """
        return self.__modifier.get_dict()

    def update_check_valid(self, new_dict: dict) -> bool:
        """
        Updates the dictionary and checks if it is valid.

        Args:
            new_dict (dict): The new dictionary to be added or updated.

        Returns:
            bool: True if the new dictionary is valid, False otherwise.
        """
        self.__validation = self.__modifier.update_check_valid(new_dict, self.__name)
        if self.__name and self.__validation: self.__validation = True
        else:                                 self.__validation = False
        return self.__validation

    def check_validation(self) -> bool:
        """
        Checks the validation status of the current dictionary.

        Returns:
            bool: True if the dictionary is valid, False otherwise.
        """
        return self.__validation

    def save_template(self) -> bool:
        """
        Saves the validated template to the templates dictionary.

        Returns:
            bool: True if the template was successfully saved, False otherwise.
        """
        try:
            if self.__validation:
                new_dict = self.__modifier.get_dict()
                self.__templates.append(new_dict[new_dict.keys()[0]])
                save_json(self.__templates_dict_path, self.__templates)
                self.__name = False
                return True
            else:
                return False
        except:
            return False

    def remove_template(self, template_name:str) -> bool:

        for row in self.__templates:
            if row["name"]==template_name:
                self.__templates.remove(row)
        save_json(self.__templates_dict_path)
