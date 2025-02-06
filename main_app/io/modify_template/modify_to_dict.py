class ModifyInsides:
    def __init__(self, initial_list=None):
        """
        Initialize the ModifyInsides with an optional initial list of dictionaries.
        """
        self.__new = initial_list if initial_list else []

    def get_dict(self) -> list:
        """
        Returns the list of dictionaries.
        """
        return self.__new

    def update_check_valid(self, new_dict: dict, name: str) -> bool:
        """
        Checks if the given dictionary has all the keys of the first dictionary in the list.
        If valid, replaces the list with a new dictionary entry.

        Args:
            new_dict (dict): Dictionary to validate and potentially overwrite the list.
            name (str): Name associated with the new dictionary.

        Returns:
            bool: True if the list was updated, False otherwise.
        """
        if self.__new and all(key in new_dict for key in self.__new[0]):
            self.__new = [{"name": name, **new_dict}]
            return True
        return False
