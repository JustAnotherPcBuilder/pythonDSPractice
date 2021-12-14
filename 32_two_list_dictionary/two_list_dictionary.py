def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """
    new_dict = {}
    values_size = len(values)
    keys_size = len(keys)
    if keys_size >= values_size:
        for i, key in enumerate(keys):
            if i < values_size:
                new_dict[key] = values[i]
            else:
                new_dict[key] = None
    elif len(keys) < len(values):
        for i, key in enumerate(keys):
            new_dict[key] = values[i]
    return new_dict