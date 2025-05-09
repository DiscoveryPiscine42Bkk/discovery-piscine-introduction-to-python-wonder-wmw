def get_red_haired_members(family_dict):
    if not isinstance(family_dict, dict):
        return []

    # Use filter to select only the red-haired members
    red_haired = filter(lambda item: isinstance(item[1], str) and item[1].lower() == 'red', family_dict.items())
    
    # Extract and return only the names (keys)
    return [first_name for first_name, _ in red_haired]
