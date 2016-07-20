
import xml.sax

class FuelPrice( xml.sax.ContentHandler ):
	def __init__(self):
		self.CurrentData = "	"
		self.gas_type = ""
		self.year = ""
		self.week = ""
		self.week_start = ""
		self.currency = ""

	def startElement(self, tag, attributes):
   		self.CurrentData = tag
		if tag == "mtc:country":
			print "*****" + attributes["country_name"]+"*****"
			#title = attributes["title"]
			#print "Title:", title

	def endElement(self, tag):
		if self.CurrentData == "mtc:gas_type":
			print "Price:", self.gas_type
		elif self.CurrentData == "mtc:year":
			print "Year:", self.year
		elif self.CurrentData == "mtc:week":
			print "Week:", self.week
		elif self.CurrentData == "mtc:week_start":
			print "Week_start:", self.week_start
		elif self.CurrentData == "mtc:currency":
			print "Currency:", self.currency
		self.CurrentData = ""

	def characters(self, content):
		if self.CurrentData == "mtc:gas_type":
			self.gas_type = content
		elif self.CurrentData == "mtc:year":
			self.year = content
		elif self.CurrentData == "mtc:week":
			self.week = content
		elif self.CurrentData == "mtc:week_start":
			self.week_start = content
		elif self.CurrentData == "mtc:currency":
			self.currency = content



if ( __name__ == "__main__"):
   
	parser = xml.sax.make_parser()
	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	Handler = FuelPrice()
	parser.setContentHandler( Handler )
   
	parser.parse("http://www.globalpetrolprices.com/api/getGasXML_weekly.php?gasoline_diesel=1&rate=USD&countries=115,120,121,122,126,133,151,153,157,160,167&p=c589d1c022e5984d0df31eedb3d4e76d")