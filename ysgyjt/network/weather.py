"""
retrieve weather information.

using info from m.weather.com.cn

"""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>
# -*- coding: utf-8 -*-


import urllib2 as ul
import json


api_address_base = 'http://m.weather.com.cn/data/'
api_address_suffix = '.html'
code_gy = '101010100'
code_bj = '101260101'
code_sh = '101020100'


def get_weather_json(geocode):
    """get weather and return json object."""
    pass


class Weather():

    """
    weather class.

    load api data according geocode

    """

    data = None

    def __init__(self, geocode=code_gy):
        self.data = json.loads(
            ul.urlopen(api_address_base +
                       geocode +
                       api_address_suffix).read())['weatherinfo']

    def get_weekday(self):
        """
        get weekday.

        return string

        """
        return self.data['week']

    def get_xc(self):
        """
        get car washing rating.

        return string

        """
        return self.data["index_xc"]

    def get_tr(self):
        """
        get trip rating.

        return string

        """
        return self.data["index_tr"]


if __name__ == '__main__':
    wea = Weather()
    print 'today is ' + wea.get_weekday()
    print 'today car washing rate is ' + wea.get_xc()
    print 'today trip rate is ' + wea.get_tr()
