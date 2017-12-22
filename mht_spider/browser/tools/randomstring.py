# -*- coding: UTF-8 -*-

try:
    import time
    from random import Random
except ImportError:
    print "import Err!!"


def get_time_13():
    """ 
    Such As: 1510556369752
    """
    t_str = time.time()
    nowTime = int(round(t_str * 1000))
    return str(nowTime)


def get_boundary_flag(randomlength=33):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    _str = ''

    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        _str += chars[random.randint(0, length)]

    _str = "----" + _str
    return _str
