import urllib2
import urllib
import re
import time

class Tool:
	removeImg = re.compile('<img.*?>| {7}|')
	removeAddr = re.compile('<a.*?>|</a>')
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
	replaceTD= re.compile('<td>')
	replacePara = re.compile('<p.*?>')
	replaceBR = re.compile('<br><br>|<br>')
	removeExtraTag = re.compile('<.*?>')
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replacePara,"\n    ",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		return x.strip()
'''
class RC:
	removeChinese = re.compile('\\\\xc4|\\\\xea|\\\\xd|\\\\xc2|\\\\xb7|\\\\xdd')
	def replace(self,x):
		x = re.sub(self.removeChinese,"",x) 
'''

class BDTB:
	def __init__(self, baseUrl,seeLZ):
		self.baseUrl = baseUrl
		#self.seeLZ = '?see_lz' + str(seeLZ)
		self.tool = Tool()


	def getPage(self,pageNum):
		try:
			url = self.baseUrl +'?p=' + str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			#print response.read()
			return response.read()#.decode('utf-8')
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"Connceting Fail, because",e.reason
				return None

	def getContent(self,page):
		pattern = re.compile('<td class="" style=\'width:;\'>(.*?)</td>',re.S)
		items = re.findall(pattern,page)
		contents = []
		for item in items:
			content = '\n' + self.tool.replace(item)
			contents.append(content)
		return contents

tempfile = open("temp-" + str(time.time()) + ".txt", "w+")

baseUrl = 'http://data.eastmoney.com/cjsj/consumerpriceindex.aspx'

for i in range(6):
	bdtb = BDTB(baseUrl,i+1)
	temp = bdtb.getContent(bdtb.getPage(i+1))
	for kkk in temp:
		tempfile.write(kkk)


tempfile.close()


