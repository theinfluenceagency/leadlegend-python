           
import requests 
import json
import urllib

headers ={}
headers["Content-Type"]='application/x-www-form-urlencoded'
endpoint = 'http://35.182.231.171:3010/api/contacts/contactSubmit'

#Convert the hs_context dictionary to a string
ll_context = json.dumps({
    "lltk": "60c2ccdfe4892f0fa0593940b12c11aa", 
    "ipAddress": "192.168.1.12", 
    "pageUrl": "http://demo.leadAPi.com/contact/", 
    "pageName": "Contact Us", 
    "redirectUrl": "http://demo.hubapi.com/thank-you/"     
})

#Build your request body
data = urllib.urlencode({
	'firstName':'test',
	'lastName':'test',
	'email':'test123@gmail.com',
	'phone':'35676543',
    'company':'sdsdsdsd',
    'message':'messagemessagemessagemessage',
	'hs_context': ll_context
	})

r = requests.post( url = endpoint, data = data, headers = headers)

print(r.text)
