class ModifyInsides:
    def __init__(self, initial_dict=None):
        """
        Initialize the ModifyInsides with an optional initial dictionary.
        """
        self.__new = initial_dict if initial_dict else {}


    def get_dict(self)->dict:
        """
        Returns the values of the 'new' dictionary.
        """
        return self.__new

    def update_check_valid(self, new_dict:dict, name:str)->bool:
        """
        Checks if the given dictionary has all the keys of the 'new' dictionary.
        If valid, overwrites 'new' with the given dictionary.

        Args:
            new_dict (dict): Dictionary to validate and potentially overwrite 'new'.

        Returns:
            bool: True if 'new' was updated, False otherwise.
        """
        if all(key in new_dict for key in self.__new):
            self.__new = {}
            self.__new[name] = new_dict.copy()
            return True
        return False

