

def plain_dict(name:str, dictionary: dict)->bool:
    
    try:
        if name in dictionary.keys():       return True
        else:                               return False
    except: return False