"""
store static config value

todo: will move config value to ini file later

"""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>
# -*- coding: utf-8 -*-

#database setting
db_url = "mysql+pymysql://gyjt:tjyg@121.199.55.129/gyjt"

#sms bechtech settings
msg_template = "{:http://sms.bechtech.cn/Api/send/data/json?accesskey={accesskey}&secretkey={secretkey}&mobile={phone}&content={message}}"
msg_upstream_recvtime = 'recvtime'
msg_upstream_mobile = 'mobile'
msg_upstream_content = 'content'



#weather api settings
api_address_base = 'http://m.weather.com.cn/data/'
api_address_suffix = '.html'
code_gy = '101260101'
code_bj = '101010100'
code_sh = '101020100'

