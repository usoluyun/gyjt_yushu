""" <docstring here>."""
#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>

from sqlalchemy import *
from ysgyjt.db import tdb_sql
from ysgyjt.appconfig import *

engine = create_engine(db_url)
meta = tdb_sql.make_meta(engine)


def get_user_table():
    """
    return mapped table user.

    join_date and isdeleted are not included.

    """
    return Table('user', meta, autoload=True, autoload_with=engine)


def insert_user_table(phone):
    """
    insert data to db.

    support mysql

    """
    saved_phone = select_user_table(phone)
    if saved_phone.fetchone() is None:
        insertion = get_user_table().insert()
        insertion.execute(phone=phone)


def select_user_table(phone):
    """
    return data from user table by filters.

    return None if no data exists

    """
    table = get_user_table()
    selection = table.select(table.c.phone == phone)
    return selection.execute()


def main():
    """main method."""
    pass

if __name__ == "__main__":
    main()
