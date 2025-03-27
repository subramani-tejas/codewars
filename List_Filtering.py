def filter_list(l):
    'return a new list with the strings filtered out'
    return [item for item in l if isinstance(item, int)]