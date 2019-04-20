#-*- coding: utf-8 -*-
# 这份爬虫用于获取 yande.re 的图片 采用 Python2.7 开发
# 写的很乱
# R18

__author__ = 'Yazawazi'

# 函数库调用（需要删去一些）
import urllib
import os
import time
import random
import xml.sax
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 定义函数
def getIt(num):

        # 创建文件夹
	path = './save'
	bool = os.path.exists('./save')
	if not bool:
		os.makedirs('./save')

        # 获取 XML 内容
        request = urllib.urlopen(url = 'https://yande.re/post.xml?tags=uncensored&page=' + str(num))
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
                print '---数据信息---'
                if post.hasAttribute('id'):
                        print '\t[#]图片编号: %s' % post.getAttribute('id')
                if post.hasAttribute("tags"):
                        print '\t[#]图片标签: %s' % post.getAttribute('tags')
                if post.hasAttribute("md5"):
                        print '\t[#]图片哈希值: %s' % post.getAttribute('md5')
                if post.hasAttribute("file_size"):
                        print '\t[#]图片大小（字节）: %s' % post.getAttribute('file_size')
                if post.hasAttribute("file_ext"):
                        print '\t[#]图片文件类型: %s' % post.getAttribute('file_ext')
                if post.hasAttribute("file_url"):
                        print '\t[#]图片地址: %s' % post.getAttribute('file_url')
		if post.hasAttribute("preview_url"):
			print '\t[#]图片浏览地址: %s' % post.getAttribute("preview_url")
		if post.hasAttribute("sample_url"):
			print '\t[#]图片小图地址: %s' % post.getAttribute("sample_url")
		
                # 下载数据
                print '---下载信息---'
		print '\t[#]正在下载...'
                url = post.getAttribute('file_url')
                print '\t[#]已获取下载地址。'
                md5 = post.getAttribute('md5')
                print '\t[#]已获取 MD5 特征码。'
                savename = url.lstrip('https://files.yande.re/image/' + md5 + '/')
                print '\t[#]已确定文件名。'
                print '\t[#]正在获取数据...'
                urllib.urlretrieve(url, './save/' + savename)
                print '\t[#]下载完毕...'


# 询问用户从第几页开始爬以及结束页码
print 'Yande.re R18 爬虫'
times = raw_input('开始:')
end = raw_input('结束:')
end = str(int(end) + 1)

# while 循环来多次执行函数
while times != end:
	# 执行函数
	getIt(times)
	# 延迟一下
	time.sleep(5)
	# 自增数值
	times = str(int(times) + 1)

# 代码结束
