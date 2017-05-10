#coding=utf-8
from bs4 import BeautifulSoup as bs
import requests

baseUrl = 'http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html'
header = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-HK;q=0.6',
		'Cache-Control':'max-age=0',
		
		'Host':'www.stats.gov.cn',
		'If-Modified-Since':'Tue, 14 Mar 2017 01:47:33 GMT',
		'If-None-Match':"2000000017ab0-b053c-54aa702fc1f21",
		'Proxy-Connection':'keep-alive',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Mobile Safari/537.36',
    }
cookie = {'Cookie':'AD_RS_COOKIE=20083361; _trs_uv=ac0l_6_j2idplzf; _trs_ua_s_1=3wng_6_j2idplze'}
res = requests.get(baseUrl,headers=header,cookies=cookie)
res.encoding = 'utf-8'
soup = bs(res.text,'html.parser')
# print soup
cName = []
cId = []
for span in soup.findAll('span',attrs={'lang':'EN-US'}):
	# print span, span.text
	cId.append(span.text.strip())
for span in soup.findAll('span',attrs={'style':'font-family: 宋体'}):
	if span.text.strip() == '':
		pass
	else:
		cName.append(span.text.strip())
dicArr = []
for i in range(cName.__len__()):
	# print cName[i] , cId[i]
	dic = {}
	dic['cId'] = cId[i]
	dic['cName'] = cName[i]
	print cId[i], cId[i][-2:] , cId[i][-4:]
	if cId[i][-4:] == '0000':
		dic['groud'] = '1'
		dic['parentId'] = '0'
	elif cId[i][-2:] == '00':
		dic['groud'] = '2'
		dic['parentId'] = cId[i][:3] + '000'
		# print cId[i][:3] + '000' , '+++++++++++' , cName[i]
	else:
		dic['groud'] = '3'
		dic['parentId'] = cId[i][:4] + '00'
		# print  cId[i][:4] + '00' , '***********' , cName[i]
	if cName[i].encode("utf-8")  == '市辖区':
		pass
	else:
		dicArr.append(dic)

print dicArr , dicArr.__len__()