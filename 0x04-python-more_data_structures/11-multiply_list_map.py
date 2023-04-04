#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    '''Returns a list with all vals mul'd by a number, without loops'''
    mul_list = []
    mul_list = list(map(lambda x: x * number, my_list))
    return mul_list
