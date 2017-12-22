# -*- coding: UTF-8 -*-
from browser.browser import Browser
from browser.tools import htmltoolmiccn, cookietool
from bs4 import BeautifulSoup
import time
import sys
import os

def down_progress(size, total_size):
    progress = (size * 100) / float(total_size)
    time.sleep(0.5)
    sys.stdout.write("[%.2f %%], %d/%dKB\r" % (progress, size, total_size))
    sys.stdout.flush()

def file_write(r, temp_filename, total_size):
    f = open(temp_filename , "wb")
    had_down_size = 0
    print "Download progress:"
    # for chunk in r.iter_content(chunk_size=512):
    for chunk in r.iter_content(chunk_size=102400):
        if chunk:
            f.write(chunk)
            len_chunk = len(chunk)/1024
            # print len_chunk
        had_down_size = had_down_size + len_chunk
        down_progress(had_down_size,total_size)







# 使用用户登陆留下的cookies，登陆应用
browser = Browser()
bbHeader={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# 
# browser.read_cookies()
# browser.read_cookies_json()
# fsrc_tools.read_remote_cookies()
browser.initBrowser(bbHeader=bbHeader)

browser.do_get("http://www.mianhuatang520.com/qb/2.htm")
print browser.response.status_code
# .decode("GBK")

soup = BeautifulSoup(browser.response.text ,'html5lib') 
# print (browser.response.text).encode("GB2312")
soup.prettify("GB2312")

li_list =  soup.select("div#newscontent > div > ul > li")
# print li_list
count = 0
for li in li_list:
    count = count + 1 
    print "============================================" 
    # print li.encode("GB2312")
    tmp_soup = BeautifulSoup(li.encode("UTF-8") ,'html5lib')
    s2_a = tmp_soup.select("[class~=s2] a")
    s2_url = s2_a[0].get('href')
    # print s2_url
    bookname = s2_a[0].get_text()
    # print type(bookname)
    bookname = bookname.encode("GBK")
    print bookname.decode("GBK")
    # print s2_url_downpage
    time.sleep(1)
    browser.bHeader['Referer'] = s2_url
    s2_url_downpage = s2_url.replace("xs","txt")
    print 's2_url_downpage',  s2_url_downpage
    browser.do_get(s2_url_downpage)
    downpage_rep_soup = BeautifulSoup(browser.response.text, 'html5lib')
    downpage_rep_soup.prettify("GB2312")
    # print downpage_rep_soup.encode("GB2312")
    downpage_a = downpage_rep_soup.select("div#main > p:nth-of-type(2) > a")
    # print 'downpage_rep_soup', downpage_move_a
    downpage_a_url = downpage_a[0].get('href')
    downpage_a_url = "http://www.mianhuatang520.com" + downpage_a_url
    print 'downpage_a_url >> ', downpage_a_url

    time.sleep(1)

    print 1
    browser.bHeader['Referer'] = s2_url_downpage
    total_size = browser.response_Headers["Content-Length"]
    print 2
    browser.do_get(downpage_a_url, stream=True)
    print 3
    downpage_move_rep = browser.response
    print 4
    time.sleep(1)
    temp_filename = "downlaod_path/"+ str(count) + ".txt"
    end_filename = "downlaod_path/"+ str(count) + "_" + bookname + ".txt"
    print temp_filename, "[ %dM]" %(int(total_size)/1024)
    file_write(downpage_move_rep, temp_filename, int(total_size))
    # file_write(downpage_move_rep, str(count) + ".txt", int(total_size))
    os.rename(temp_filename,end_filename)

