def reverse_sort_dictionary(names):
    items = list(names.items())
    items.sort(reverse=True)
    sorted_dict = dict(items)
    return  [(name, values[0]) for name, values in sorted_dict.items()]




names = {'Tom': (5464512, 24), 'Mary': (1557896, 20), 'Sara': (5446987, 32)}
new_list = reverse_sort_dictionary(names)
for x in new_list:
    print(x)        
