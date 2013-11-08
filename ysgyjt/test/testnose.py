"""
Test nose function.

using nose

"""

#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>


def TestNoseSuccess():
    """
    test if nose is working.

    assert true

    """
    a = 1
    b = 1
    assert a == b


def TestNoseFailed():
    """
    test if nose is working.

    assert false

    """
    a = 1
    b = 2
    assert a != b
