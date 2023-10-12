def reverse_sort_dictionary(names):
    items = list(names.items())
    items.sort(reverse=True)
    sorted_dict = dict(items)
    return  [(name, values[0]) for name, values in sorted_dict.items()]





