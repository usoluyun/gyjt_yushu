#coding: utf-8
"""
a sms.bechtech.cn api wrapper module.

message will be logged in flat file

"""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>

import urllib2 as ul
from ysgyjt.appconfig import *
from ysgyjt.network.weather import *
import json


class Smsbechtech():

    """
    a sms bechtech message wrapper.

    has message send and logging

    """

    content = ""
    mobile = ""

    def __init__(self, weather, p):

        self.content = contenttemplate.decode('utf-8') % (weather.get_city(),
                                          weather.get_today_weather(),
                                          weather.get_today_highest_temp(),
                                          weather.get_today_lowest_temp(),
                                          weather.get_tomorrow_weather(),
                                          weather.get_tomorrow_highest_temp(),
                                          weather.get_tomorrow_lowest_temp())

        #self.content = "【你好，陆贇】"
        #self.content.encode('utf-8')
        self.mobile = p

    def send(self):
        url = msg_sendurl % (accesstoken, secretkey, self.mobile, self.content)
        return json.loads(ul.urlopen(url.encode('utf-8')).read())['result']

if __name__ == '__main__':
    msg = Smsbechtech(Weather(), "13601844147")
    result = msg.send()
    print result




