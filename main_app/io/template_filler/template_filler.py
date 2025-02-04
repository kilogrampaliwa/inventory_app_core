#from main_app.io.template_filler.modifcation_dict_template import ModifcationDictTemplate
from main_app.utils import load_json, plain_dict

class TemplateFiller:

    def __init__(self, templates_dict_path: str, template_name: str = "none"):
        """
        Initializes the TemplateFiller object.

        Args:
            template_name (str): The name of the template.
            templates_dict_path (str): Path to the JSON file containing templates.

        Raises:
            ValueError: If the provided template_name does not exist in the templates.
        """
        self.__templates_dict_path = templates_dict_path
        self.__templates = load_json(templates_dict_path)
        self.__validation = False

        if template_name!="none":   self.__call__(template_name)

    def __call__(self, template_name: str):
        """
        Initializes the TemplateFiller object.

        Args:
            template_name (str): The name of the template.
            templates_dict_path (str): Path to the JSON file containing templates.

        Raises:
            ValueError: If the provided template_name does not exist in the templates.
        """
        self.__validation = False

        from main_app.io.template_filler.modifcation_dict_template import ModifcationDictTemplate

        if plain_dict(template_name): pass
        else: raise ValueError("TemplateFiller: template_name doesn't exist.")

        self.__modifier = ModifcationDictTemplate(self.__templates[template_name])

    def get_flattened_dict(self):
        """
        Retrieves a flattened version of the template dictionary.

        Returns:
            dict: A flattened dictionary representation of the template.
        """
        return self.__modifier.get_flattened_dict()

    def get_flattened_whole_dict(self):
        """
        Retrieves a flattened version of the template dictionary.

        Returns:
            dict: A flattened dictionary representation of the template.
        """
        return self.__modifier.flatten_dict(self.__templates)

    def check_values_not_empty(self) -> bool:
        """
        Checks whether all values in the template dictionary are non-empty.

        Returns:
            bool: True if all values are non-empty, False otherwise.
        """
        self.__validation = self.__modifier.check_values_not_empty()
        return self.__validation

    def create_proper_dict(self, flattened_dict: dict) -> bool:
        """
        Constructs a proper hierarchical dictionary from a flattened dictionary.

        Args:
            flattened_dict (dict): The flattened dictionary to convert.

        Returns:
            bool: True if the proper dictionary was successfully created, False otherwise.
        """
        self.__validation = self.__modifier.create_proper_dict(flattened_dict)
        return self.__validation

    def give_dict(self) -> dict:
        """
        Provides the constructed template dictionary if valid.

        Returns:
            dict: The constructed hierarchical dictionary.

        Raises:
            ValueError: If the dictionary is invalid or contains empty values.
        """
        if self.__validation:
            return self.__modifier.give_dict()
        else:
            raise ValueError("TemplateFiller: proper dictionary not created, probably empty spaces left.")
