def clean_bom_keys(dict_list):
    """
    Cleans the BOM (Byte Order Mark) from the keys of dictionaries in a list.
    """
    return [
        {key.lstrip('\ufeff'): value for key, value in d.items()}
        for d in dict_list
    ]