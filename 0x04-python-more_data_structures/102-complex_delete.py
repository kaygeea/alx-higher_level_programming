#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_list = list(a_dictionary.keys())

    for dict_vals in keys_list:
        if value == a_dictionary.get(dict_vals):
            del a_dictionary[dict_vals]

    return (a_dictionary)
