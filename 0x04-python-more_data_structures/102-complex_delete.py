#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value:
        new_dict = {key: val for key, val in a_dictionary.items()
                if val is not value}
        return (new_dict)
    return (a_dictionary)
