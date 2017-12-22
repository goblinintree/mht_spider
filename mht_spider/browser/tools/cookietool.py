# -*- coding: UTF-8 -*-

import time
import requests
import os

def tuple_from_sioncookie(sioncookie):
    cookie_tuple = (sioncookie.name,sioncookie.value,sioncookie.domain)
    return cookie_tuple

def list_tuple_from_sioncookies(sioncookies):
    cookie_list = []
    if len(sioncookies) > 0:

        for tmp_cookie in sioncookies:
            cookie_list.append(tuple_from_sioncookie(tmp_cookie))
            pass
        pass
    return cookie_list

def sioncookies_from_tuple_list(cookie_tuple_list, sioncookies=None, overwrite=True):
    """Returns a CookieJar from a key/value dictionary.

    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :param cookiejar: (optional) A cookiejar to add the cookies to.
    :param overwrite: (optional) If False, will not replace cookies
        already in the jar with new ones.
    """
    if sioncookies is None:
        sioncookies = requests.cookies.RequestsCookieJar()
        # cookiejar = src_cookie_jar

    if cookie_tuple_list is not None:
        names_from_jar = [cookie.name for cookie in sioncookies]
        for cookie_tuple in cookie_tuple_list:
            tup_name = cookie_tuple[0]
            tup_value = cookie_tuple[1]
            tup_domain = cookie_tuple[2]
            if overwrite or (tup_name not in names_from_jar):
                sioncookies.set_cookie(yala_create_cookie(tup_name, tup_value, domain=tup_domain))
    return sioncookies

def sioncookies_from_cookiejars(cj):
    """Returns a key/value dictionary from a CookieJar.

    :param cj: CookieJar object to extract cookies from.
    :rtype: dict
    """
    sioncookies = requests.cookies.RequestsCookieJar()
    sioncookies.update(cj)
    return sioncookies

def do_print(name="Yola"):
    print name
    pass
do_print()



def save_remote_cookies(string_data, file_path, file_name="cookies_default.txt"):
    issuccess = False
    f = file(os.path.join(file_path, file_name), "w+")
    f.writelines(string_data)
    f.close()

    issuccess = True
    return issuccess


def read_remote_cookies(file_path, file_name="cookies_default.txt"):
    string_data = ""
    try:
        f = open(os.path.join(file_path, file_name))
        print 1
        tmp_line = f.readline()
        while tmp_line: 
            string_data = string_data + tmp_line
            print tmp_line
            tmp_line = f.readline() 

    except Exception as r:
        r.message
        string_data =""
    finally:
        f.close() 
    return string_data

def parser_cookies(cookies_string):
    """
    pid=TguMjQwLjI2LjIwMzIwMTcxMjAxMTQxNzM4NjI3MTc3Nzk3NzYN; sf_img=AM; ordr=1; 
    split 
    """
    cookie_dict = {}
    if cookies_string:
        cookie_list = cookies_string.split(";")
        for cookie in cookie_list:
            cookie_dict[str(cookie.partition("=")[0]).encode("UTF-8")] = str(cookie.partition("=")[2]).encode("UTF-8")
    # print cookie_dict
    return cookie_dict

if __name__ == "__main__":
    file_dict = eval(read_remote_cookies("e:\myspace\space_fsrc\Django-Web\yola\scripts\scripts\\browser\cookies", "cookies_json3.txt"))
    # print read_remote_cookies("e:\myspace\space_fsrc\Django-Web\yola\scripts\scripts\\browser\cookies", "cookies_json3.txt")
    cookies_string = file_dict["u_cookie"]
    parser_cookies(cookies_string)























def yala_create_cookie(name, value, **kwargs):
    """Make a cookie from underspecified parameters.

    By default, the pair of `name` and `value` will be set for the domain ''
    and sent on every request (this is sometimes called a "supercookie").
    """
    result = dict(
        version=0,
        name=name,
        value=value,
        port=None,
        domain='',
        path='/',
        secure=False,
        expires=None,
        discard=True,
        comment=None,
        comment_url=None,
        rest={'HttpOnly': None},
        rfc2109=False,)

    badargs = set(kwargs) - set(result)
    if badargs:
        err = 'create_cookie() got unexpected keyword arguments: %s'
        raise TypeError(err % list(badargs))

    result.update(kwargs)
    result['port_specified'] = bool(result['port'])
    result['domain_specified'] = bool(result['domain'])
    result['domain_initial_dot'] = result['domain'].startswith('.')
    result['path_specified'] = bool(result['path'])

    return requests.cookies.cookielib.Cookie(**result)

def dict_from_cookiejar(cj):
    """Returns a key/value dictionary from a CookieJar.

    :param cj: CookieJar object to extract cookies from.
    :rtype: dict
    """

    cookie_dict = {}

    for cookie in cj:
        cookie_dict[cookie.name] = cookie.value

    return cookie_dict