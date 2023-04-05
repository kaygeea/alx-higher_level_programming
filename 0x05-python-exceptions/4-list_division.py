#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    '''Divides elems in list 1 by elems in list 2, using exception handling'''
    my_list_3 = []
    for elems in range(0, list_length):
        try:
            val = my_list_1[elems] / my_list_2[elems]
        except TypeError:
            print("wrong type")
            val = 0
        except ZeroDivisionError:
            print("division by 0")
            val = 0
        except IndexError:
            print("out of range")
            val = 0
        finally:
            my_list_3.append(val)
    return (my_list_3)
