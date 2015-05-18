#!/usr/bin/env python

 #if this doesn't run, then try 'pip install requests'
import requests

class Base:
	def __init__(self):
		self.code = ""
		self.shortDesc = ""
	def debug(self):
		print "code = " + self.code
		print "shortDesc = " + self.shortDesc

class Item(Base):
	def __init__(self):
		self.code = "0000"
		self.shortDesc = "Item"

class Wheel(Item):
	def __init__(self):
		self.code = "001337"
		self.shortDesc = "Wheel"

def main():
	w = Wheel()
	w.debug()

	#this is a simple get example
	try:
		res = requests.get('http://www.google.com')
		res.raise_for_status()
		print res.text

		#if it is json...
		data = res.json()
		print data
	except ValueError as e:
		#catches value errors..example, if we wanted json and it couldn't decode it
		print "Value Error: ", e.message
	except requests.exceptions.HTTPError as e:
		 print "HTTP Error:", e.message
	except requests.exceptions.ConnectionError as e:
		print "Connection Error:", e.message
if __name__ == "__main__":
    main()