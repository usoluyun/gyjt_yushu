__author__ = 'luyun'

import sqlalchemy as sa
from datetime import datetime
import logging
import threading
import sys

log_format = logging.Formatter('sql: %(message)s')
metaecho = False #if print out in stdout

class TransactionSet(threading.local):
    """A manager for SQL transactions.

    This implements a thread local meta-transaction which may span multiple
    databases.  The existing tdb_sql code calls add_engine before executing
    writes.  If thing.py calls begin then these calls will actually kick in
    and start a transaction that must be committed or rolled back by thing.py.

    Because this involves creating transactions at the connection level, this
    system implicitly relies on using the threadlocal strategy for the
    sqlalchemy engines.

    This system is a bit awkward, and should be replaced with something that
    doesn't use module-globals when doing a cleanup of tdb_sql.

    """

    def __init__(self):
        self.transacting_engines = set()
        self.transaction_begun = False

    def begin(self):
        """Indicate that a transaction has begun."""
        self.transaction_begun = True

    def add_engine(self, engine):
        """Add a database connection to the meta-transaction if active."""
        if not self.transaction_begun:
            return

        if engine not in self.transacting_engines:
            engine.begin()
            self.transacting_engines.add(engine)

    def commit(self):
        """Commit the meta-transaction."""
        try:
            for engine in self.transacting_engines:
                engine.commit()
        finally:
            self._clear()

    def rollback(self):
        """Roll back the meta-transaction."""
        try:
            for engine in self.transacting_engines:
                engine.rollback()
        finally:
            self._clear()

    def _clear(self):
        self.transacting_engines.clear()
        self.transaction_begun = False


transactions = TransactionSet()


def make_meta(engine):
    metadata = sa.MetaData(engine)
    metadata.bind.echo = metaecho
    return metadata


def  create_table(table, index_commands=None):
    t = table
    if not t.bind.has_table(t.name):
        t.create(checkfirst=False)
        if index_commands:
            for i in index_commands:
                t.bind.execute(i)


def index_commands(table, type):
    commands = []
    pass
