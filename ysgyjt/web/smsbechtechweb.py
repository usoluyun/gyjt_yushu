#coding: utf-8
"""
receive upstream from smsbechtech

using tornado
"""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>

import tornado.ioloop
import tornado.web
from ysgyjt.model import upstreammsg
from ysgyjt.appconfig import *


class UpstreamHandler(tornado.web.RequestHandler):
    def get(self):
        redvtime = self.get_argument('recvtime')
        mobile = self.get_argument('mobile')
        content = self.get_argument('content')
        msg = upstreammsg.UpstreamMsg(redvtime, mobile, content)
        msg.insert_upstream_table()

application = tornado.web.Application([
    (r"/upstream", UpstreamHandler),
])

if __name__ == "__main__":
    application.listen(web_port)
    tornado.ioloop.IOLoop.instance().start()