"""
Test upstream  function.

using nose

"""

#!/usr/bin/python
#Filename:
#author: Chester LU <usoluyun@gmail.com>


from model.upstreammsg import *


def TestSaveUpstream():
    """
    test if save upstream is working

    assert true

    """
    msg = UpstreamMsg("2013-1-1 10:00:00", "8613601844147", "hello world!")
    msg.insert_upstream_table()

    result = UpstreamMsg.select_upstream_table("8613601844147")

    assert result.fetchone() is not None

if __name__ == '__main__':
    TestSaveUpstream()
