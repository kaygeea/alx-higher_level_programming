#!/usr/bin/python3
def remove_char_at(str, n):
    '''Creates a cpy of str, removing the char(s) at position n'''
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
