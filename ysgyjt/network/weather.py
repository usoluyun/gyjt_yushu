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
from appconfig import *




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

    def get_today_highest_temp(self):
        """
        get today highet temp.

        return string

        """
        t1 = self.data['temp1']
        return t1[:t1.index('~')]

    def get_today_lowest_temp(self):
        """
        get today lowest temp.

        return string

        """
        t1 = self.data['temp1']
        return t1[t1.index('~') + 1:]

    def get_tomorrow_highest_temp(self):
        """
        get tomorrow highet temp.

        return string

        """
        t2 = self.data['temp2']
        return t2[:t2.index('~')]

    def get_tomorrow_lowest_temp(self):
        """
        get tomorrow lowest temp.

        return string

        """
        t2 = self.data['temp2']
        return t2[t2.index('~') + 1:]

    def get_city(self):
        """
        get city name.

        return string

        """
        return self.data['city']

    def get_today_weather(self):
        """
        get today's weather.

        return string

        """
        return self.data['weather1']

    def get_tomorrow_weather(self):
        """
        get tomorrow weather.

        return string

        """
        return self.data['weather2']

if __name__ == '__main__':
    wea = Weather()
    print 'today is ' + wea.get_weekday()
    print 'today car washing rate is ' + wea.get_xc()
    print 'today trip rate is ' + wea.get_tr()
    print 'today highest temp is ' + wea.get_today_highest_temp()
    print 'today lowest temp is ' + wea.get_today_lowest_temp()
    print 'tomorrow highest temp is ' + wea.get_tomorrow_highest_temp()
    print 'tomorrow lowest temp is ' + wea.get_tomorrow_lowest_temp()
    print 'city is ' + wea.get_city()
    print 'today weather is ' + wea.get_today_weather()
    print 'tomorrow weather is ' + wea.get_tomorrow_weather()
