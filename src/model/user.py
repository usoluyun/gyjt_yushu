""" <docstring here>."""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>

from sqlalchemy import *
from db import tdb_sql

engine = create_engine("mysql+pymysql://gyjt:tjyg@121.199.55.129/gyjt")
meta = tdb_sql.make_meta(engine)


def get_user_table(metadata):
    """
    return mapped table user.

    join_date and isdeleted are not included.

    """
    return Table('user',
                 metadata,
                 Column('id', Integer, primary_key=True),
                 Column('phone', Unicode(20)),
                 Column('carrier', Unicode(20)))


def insert_user_table(phone):
    """
    insert data to db.

    support mysql

    """
    insertion = get_user_table(meta).insert()
    insertion.execute(phone='phone')


def select_user_table(phone):
    """
    return data from user table by filters.

    return None if no data exists

    """
    table = get_user_table(meta)
    selection = table.select(table.c.phone == phone)
    return selection.execute()


def main():
    """main method."""
    pass

if __name__ == "__main__":
    main()
