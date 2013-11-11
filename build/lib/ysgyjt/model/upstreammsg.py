"""
retrieve upstream message and saved in database

using info from m.weather.com.cn

"""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>
# -*- coding: utf-8 -*-


from sqlalchemy import *
from ysgyjt.db import tdb_sql
from ysgyjt.appconfig import *

engine = create_engine(db_url)
meta = tdb_sql.make_meta(engine)


class UpstreamMsg():
    """
    upstream message class

    sms.bechtech.com upstream api

    """
    recvtime = ''
    mobile = ''
    content = ''

    def __init__(self, t, p, c):
        self.recvtime = t
        self.mobile = p
        self.content = c

    @staticmethod
    def get_upstreammsg_table():
        """
        return mapped table upstream message.

        return void

        """
        return Table('upstreammsg', meta, autoload=True, autoload_with=engine)

    def insert_upstream_table(self):
        """
        insert data to db.

        support mysql

        """
        upstream_msg_insertion = self.get_upstreammsg_table().insert()
        upstream_msg_insertion.execute(recvtime=self.recvtime, mobile=self.mobile, content=self.content)

    @staticmethod
    def select_upstream_table(phone):
        """
        return data from user table by filters.

        return None if no data exists

        """
        table = UpstreamMsg.get_upstreammsg_table()
        if phone:
            selection = table.select(table.c.mobile == phone)
        else:
            selection = table.select()
        return selection.execute()


def main():
    """main method."""
    pass

if __name__ == "__main__":
    main()
