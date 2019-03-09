#-*- coding: utf-8 -*-
# 这份爬虫用于获取 yande.re 的图片 采用 Python2.7 开发
# 写的很乱不要建议

__author__ = 'Yazawazi'

# 函数库调用（需要删去一些）
import urllib
import re
import os
import time
import random
import xml.sax
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
reload(sys)
sys.setdefaultencoding('gb18030')

# 定义函数
def getIt(num):

        # 创建文件夹
	path = './save'
	bool = os.path.exists('./save')
	if not bool:
		os.makedirs('./save')

        # 获取 XML 内容
        request = urllib.urlopen(url = 'https://yande.re/post.xml?page=' + str(num))
        info = request.read()

        # 将 XML 写到文件
        with open('./' + str(num) + '.xml', 'w') as fp:
                fp.write(info)

        # 打开 XML
        domTree = xml.dom.minidom.parse('./' + str(num) + '.xml') 
        collection = domTree.documentElement

        # 获取所有 POST
        posts = collection.getElementsByTagName('post')

        # 使用 for 循环分析 post
        for post in posts:
                # 打印数据
                print '---返回数据如下---'
                if post.hasAttribute('id'):
                        print '\t[#]该图片ID为: %s' % post.getAttribute('id')
                if post.hasAttribute("tags"):
                        print '\t[#]该图片标签为: %s' % post.getAttribute('tags')
                if post.hasAttribute("md5"):
                        print '\t[#]该图片MD5码为: %s' % post.getAttribute('md5')
                if post.hasAttribute("file_size"):
                        print '\t[#]该图片字节大小为: %s' % post.getAttribute('file_size')
                if post.hasAttribute("file_ext"):
                        print '\t[#]该图片类型为: %s' % post.getAttribute('file_ext')
                if post.hasAttribute("file_url"):
                        print '\t[#]该图片储存地址为: %s' % post.getAttribute('file_url')
                # 下载数据
                print '---下载状态如下---'
		print '\t[#]正在下载中...'
                url = post.getAttribute('file_url')
                md5 = post.getAttribute('md5')
                savename = url.lstrip('https://files.yande.re/image/' + md5 + '/')
                urllib.urlretrieve(url, './save/' + savename)
                print '\t[#]完成下载'


# 询问用户从第几页开始爬以及结束页码
times = raw_input('从第几页开始爬取:')
end = raw_input('到第几页结束爬取:')

# while 循环来多次执行函数
while times != end:
	# 执行函数
	getIt(times)
	# 延迟一下
	time.sleep(5)
	# 自增数值
	times = times + 1


# 代码结束
