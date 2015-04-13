import requests #if this doesn't run, then try 'pip install requests'

def main():
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