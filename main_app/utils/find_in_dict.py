

def plain_dict(name:str, list_dictionaries: list[dict])->bool:

    try:
        for dictionary in list_dictionaries:
            if dictionary['name'] == name:                   return True
            else:                               return False
    except: return False