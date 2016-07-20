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
	replaceTags = re.compile('(Day)|T|M|SLP|H|[PP]|V|(VM)|G|RA|S|N|F')
	replancem = re.compile("m")
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replacePara,"\n",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		x = re.sub(self.replaceTags,"",x)
		x = re.sub(self.replancem,"Here comes another month",x)
		return x.strip()

class weather:
	def __init__(self, WeatherStationNo):
		self.WSN = WeatherStationNo
		self.baseUrl = 'http://en.tutiempo.net/climate/'
		self.tool = Tool()

	def getPage(self, Year, Month):
		try:
			url = self.baseUrl + Month + '-' + Year +'/ws-' + self.WSN + ".html"
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			#print response.read()
			return response.read()
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"Connceting Fail, because",e.reason
				return None

	def getContent(self,page, year,month):
		pattern = re.compile('<table cellpadding="0" class="medias mensuales" style="width:100%;" cellspacing="0">(.*?)<th colspan="15" style="height:30px;">',re.S)
		items = re.findall(pattern,page)
		contents = []
		for item in items:
			content = '\n' + self.tool.replace(item)
			print content
			Date = '\n' + year + '/' + month + '/01'
			contents.append(Date + '\t' + content)
		return contents			



Cities = {"Shanghai":'583620',"Bombay":'430030',"Sydney":'947680',"Bangkok": '484550'}

#print SH.getPage("2016","06")

MMMonth = ['01','02','03','04','05','06','07','08','09','10','11','12']
YYYear = ['2012','2013','2014','2015','2016']

for key in Cities.keys():
	tempfile = open(key + "_" + str(time.time()) + ".txt","w+")
	tempfile.write("City of " + key + ", WSN: " + Cities[key])
	for year in YYYear:
		for month in MMMonth:
			if (year == "2016" and month == "07"):
				break
			currentciti = weather(Cities[key])	
			temp = currentciti.getContent( currentciti.getPage(year,month),year, month )
			for kkk in temp:
				tempfile.write(kkk)
	tempfile.close()

#SH.getContent( SH.getPage("2016","06") )

