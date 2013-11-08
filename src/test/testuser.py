"""
test user.py.

insert and select user

"""

#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>


from model import user


def testUserInsertSelect():
    """
    test user table insert & select.

    test number 8613601844148

    """
    user.insert_user_table("8613601844147")

    result = user.select_user_table("8613601844147")

    assert result.fetchone() is not None


if __name__ == '__main__':
    testUserInsertSelect()
