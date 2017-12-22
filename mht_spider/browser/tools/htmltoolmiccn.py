# -*- coding: UTF-8 -*-

import re

pattern= r'createHiddenIframe(\(.*\)).*createHiddenIframe(\(.*\)).*createHiddenIframe(\(.*\));'
def tuple_search_from_string(pattern, string):
    tmp_tuple =()
    searchObj = re.search(pattern, string, re.M|re.I|re.S) 
    if searchObj != None:
        tmp_tuple =   searchObj.groups()
        print searchObj
        pass
    else:
        print "matchObj_items ERROR: searched None"
        pass
    return tmp_tuple

pattern = r"'scriptId':'ssoscript0'"
def list_findall_from_string(pattern, string):
    tmp_list = []
    matchObj = re.findall(pattern, string, re.M|re.I|re.S) 
    if matchObj != None:
        tmp_list = matchObj
        if len(tmp_list) > 0:
            return tmp_list
            pass
        else:
            print u"logon error"
            exit
            pass
        pass
    else:
        print u"logon error"
        exit
        pass
    return tmp_list

def contain_subString(subString, srcstring):
    if srcstring.find(subString) == -1:
        return False
    else:
        return True



# def do_test():
#     print contain_subString("yui", "asdadadadadadsa asdadad asdads dsada yulikui")
#     pass

# do_test()