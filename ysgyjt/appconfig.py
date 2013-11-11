#coding: utf-8
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>


#database setting
db_url = "mysql+pymysql://gyjt:tjyg@121.199.55.129/gyjt"


#sms bechtech settings
msg_sendurl = "http://sms.bechtech.cn/Api/send/data/json?accesskey=%s&secretkey=%s&mobile=%s&content=%s"
msg_upstream_recvtime = 'recvtime'
msg_upstream_mobile = 'mobile'
msg_upstream_content = 'content'

accesstoken = '1204'
secretkey = '0c3b4894837bcac1e7464ed3ee217611ab07096f'


#weather api settings
api_address_base = 'http://m.weather.com.cn/data/'
api_address_suffix = '.html'
code_gy = '101260101'
code_bj = '101010100'
code_sh = '101020100'

#messagecontent
contenttemplate = "【气象台】%s今天%s，最高%s，最低%s，明天%s，最高%s，最低%s"

