#!/usr/bin/python

# Sending SMS with Blueface

from mechanize import Browser
import sys

# User
user = "MyUser"
password = "$ekrit"

# URL
url = 'https://customers.blueface.ie'
urlsms = "https://customers.blueface.ie/sms.aspx"


def sendsms(number, msg):
	browser = Browser()

	browser.addheaders = [
		('user-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:19.0) Gecko/20100101 Firefox/19.0'),
		('accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
		('X-Requested-With', 'XMLHttpRequest'),
		('X-Prototype-Version', '1.6.0.2')]


        # Login form
        response = browser.open(url)
	browser.form = list(browser.forms())[0]
        browser.form['username'] = user
        browser.form['password'] = password
        browser.submit()


        # Send SMS
        response = browser.open(urlsms)
	browser.form = list(browser.forms())[0]
        browser.form['message'] = msg
	browser.form['destination'] = number
        browser.submit()
	
	#response = browser.response()
	#print response.read()


if len(sys.argv) < 2:
        print "Usage: " + sys.argv[ 0 ] + " number(s) message"
	print " - number(s) : Enter 1 or up to 100 Phone Numbers (separated by a comma)"
	print " - message : message to be sent by SMS (up to 159 chars)"
else:
        sendsms( sys.argv[ 1 ], sys.argv[ 2 ])
