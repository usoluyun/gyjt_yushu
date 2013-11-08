"""
a sms.bechtech.cn api wrapper module.

message will be logged in flat file

"""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>
# -*- coding: utf-8 -*-


import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s')


class Smsbechtech():

    """
    a sms bechtech message wrapper.

    has message send and logging

    """

    msg = ""

    def __init__(self, weather):
        pass
