class ModifcationDictTemplate:
    def __init__(self, input_dict, zero_values=True):

        # Store the original dictionary
        self.__original_dict = input_dict
        self.__validation = False
        # Create a flattened dictionary with empty string values
        self.__flattened_dict = self.flatten_dict(self.__original_dict)
        if zero_values:
            # Replace all values with empty strings
            self.__flattened_dict = {key: "" for key in self.__flattened_dict}
        # New dict
        self.__new_dict = {}

    def flatten_dict(self, d, parent_key="", sep="/")->dict:
        """
        Recursively flatten a multi-level dictionary.
        """
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(self.flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    def get_flattened_dict(self)->dict:
        """
        Return the flattened dictionary.
        """
        return self.__flattened_dict

    def check_values_not_empty(self)->bool:
        """
        Check if all values in the flattened dictionary are non-empty.
        """
        self.__validation = all(value != "" for value in self.__flattened_dict.values())
        return self.__validation

    def create_proper_dict(self, input_dict)->bool:
        """
        Create an input-like multi-level dictionary from a flattened table.
        """
        self.check_values_not_empty()
        if self.__validation:
            flattened_table = input_dict
            new_dict = {}
            for key, value in flattened_table.items():
                keys = key.split('/')
                d = new_dict
                for part in keys[:-1]:
                    d = d.setdefault(part, {})
                d[keys[-1]] = value
            self.__new_dict = new_dict
            return True
        return False

    def give_dict(self)->dict:
        """
        Returns newly created dict of original form.
        """
        return self.__new_dict
    
