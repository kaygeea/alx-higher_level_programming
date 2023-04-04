#!/usr/bin/python3

def raise_exception_msg(message=""):
    '''Raises a NameError exception, along with a debugging message.'''

    raise NameError('{}'.format(message))
