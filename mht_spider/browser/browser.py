# -*- coding: UTF-8 -*-
import requests
import cookielib
import os
from tools import cookietool
from requests.auth import HTTPProxyAuth

class Browser():

    def __init__(self):
        self.bSession = requests.Session() 
        self.bUrl = ""
        self.bData = None
        self.bHeader = None
        self.bcookies = None
        self.response = None
        self.response_Headers = None

        self.__cookies_name = "cookies" # cookies/cookies.txt
        self.__cookies_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "cookies/cookies.txt") 
        # proxy_string = 'http://yulikui:123456yu@192.168.16.189:8080'
        # self.bSession.proxies = {"http": proxy_string , "https": proxy_string}
        # self.bSession.auth = HTTPProxyAuth("yulikui","123456yu")


        print 
        pass


    def default_initBrowser(self, bbHeader=None, bbcookies=None):
        self.bHeader = bbHeader
        self.bcookies = bbcookies
        print "default_initBrowser"
        pass

    def initBrowser(self, **kwargs):
        """
        bbHeader=None, bbcookies=None
        """
        self.default_initBrowser(**kwargs)
        return self

    # def request(self, method, url,
    #         params=None, data=None, headers=None, cookies=None, files=None,
    #         auth=None, timeout=None, allow_redirects=True, proxies=None,
    #         hooks=None, stream=None, verify=None, cert=None, json=None):

    # def save_cookies(self):
    #     # new_cookie_jar = tools.YolaCookieJar(self.__cookies_path)
    #     new_cookie_jar = cookielib.LWPCookieJar(self.__cookies_path)
    #     #将转换成字典格式的RequestsCookieJar（这里我用字典推导手动转的）保存到LWPcookiejar中
    #     # for c in self.bSession.cookies:
    #     #     print c.name, ":", c.value, "==>", c.domain
    #     #     pass
    #     # requests.utils.cookiejar_from_dict({c.name: c.value for c in self.bSession.cookies}, new_cookie_jar)
    #     #保存到本地文件
    #     new_cookie_jar.save(self.__cookies_path, ignore_discard=True, ignore_expires=True)
    #     pass

    # def read_cookies(self):
    #     #实例化一个LWPCookieJar对象
    #     load_cookiejar = cookielib.LWPCookieJar()
    #     #从文件中加载cookies(LWP格式)
    #     load_cookiejar.load(self.__cookies_path, ignore_discard=True, ignore_expires=True)
    #     #工具方法转换成字典
    #     load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)
    #     #工具方法将字典转换成RequestsCookieJar，赋值给session的cookies.
    #     self.bSession.cookies = requests.utils.cookiejar_from_dict(load_cookies)
    #     pass


    def save_cookies(self):
        # new_cookie_jar = tools.YolaCookieJar(self.__cookies_path)
        new_cookie_jar = cookielib.LWPCookieJar(self.__cookies_path)
        #将转换成字典格式的RequestsCookieJar（这里我用字典推导手动转的）保存到LWPcookiejar中
        cookietool.sioncookies_from_tuple_list(cookietool.list_tuple_from_sioncookies(self.bSession.cookies), new_cookie_jar)
        #保存到本地文件
        # self.bcookies = new_cookie_jar._cookies
        new_cookie_jar.save(self.__cookies_path, ignore_discard=True, ignore_expires=True)
        pass

    def read_cookies(self):
        #实例化一个LWPCookieJar对象
        load_cookiejar = cookielib.LWPCookieJar(self.__cookies_path)
        #从文件中加载cookies(LWP格式)
        try:
            load_cookiejar.load(self.__cookies_path, ignore_discard=True, ignore_expires=True)
            pass
        except EnvironmentError as e:
            print e.message
            pass
        else:
            load_cookiejar = cookietool.sioncookies_from_cookiejars(load_cookiejar)
            pass
        #工具方法转换成字典
        # load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar._cookies)
        #工具方法将字典转换成RequestsCookieJar，赋值给session的cookies.
        self.bcookies = load_cookiejar
        self.bSession.cookies = load_cookiejar
        pass

    def read_cookies_json(self):
        #实例化一个LWPCookieJar对象
        print os.path.join(os.path.dirname(self.__cookies_path), "cookies_json3.txt")


        file_dict = eval(cookietool.read_remote_cookies(os.path.dirname(self.__cookies_path),"cookies_json3.txt"))
        cookies_string = file_dict["u_cookie"]
        cookie_dict = cookietool.parser_cookies(cookies_string)
        requests.utils.add_dict_to_cookiejar(self.bSession.cookies, cookie_dict)

        self.bcookies = self.bSession.cookies
        pass




    def do_get(self, url, **kwargs):
        """
        do_get 用户不需要自己设置header和cookies。默认使用Browser自带的参数值。
        bHeader 是 初始化是完成的；
        bcookies 是上次请求后保存的
        url * 为必填项
        注意： 所以在调用前请先确保bHeader、bcookies已经设置正确
        """
        # sion = requests.Session() 
        self.response = self.bSession.get(url,headers=self.bHeader, cookies=self.bcookies, **kwargs)
        self.bcookies = self.response.cookies
        self.response_Headers = self.response.headers

        return self

    def do_get_diy(self, url, **kwargs):
        """
        do_get_diy 中header和cookies 默认为空。
        url * 为必填项

        下面参数的使用，必须自定义
        params=None, data=None, headers=None, cookies=None, files=None,
        auth=None, timeout=None, allow_redirects=True, proxies=None,
        hooks=None, stream=None, verify=None, cert=None, json=None

        """
        # sion = requests.Session() 
        self.response = self.bSession.get(url,**kwargs)
        self.bcookies = self.response.cookies
        return self

    def do_post(self, url, data, **kwargs):
        """
        do_post 用户不需要自己设置header和cookies。默认使用Browser自带的参数值。
        bHeader 是 初始化是完成的；
        bcookies 是上次请求后保存的
        url * 为必填项
        data * 为必填项

        注意： 所以在调用前请先确保bHeader、bcookies已经设置正确
        """
        # sion = requests.Session() 
        print 10
        print data
        self.response = self.bSession.post(url, data=data, headers=self.bHeader, cookies=self.bcookies, **kwargs)
        self.bcookies = self.response.cookies
        return self
    
    def do_post_diy(self, url, data, json=None, **kwargs):
        """
        do_post_diy 中header和cookies 默认为空。
        url * 为必填项
        data * 为必填项

        下面参数的使用，必须自定义
        params=None, headers=None, cookies=None, files=None,
        auth=None, timeout=None, allow_redirects=True, proxies=None,
        hooks=None, stream=None, verify=None, cert=None, json=None
        """
        # sion = requests.Session() 
        # sion.post(url, **kwargs)
        self.response = self.bSession.post(url, data=data, json=None, **kwargs)
        self.bcookies = self.response.cookies
        return self