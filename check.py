import requests
import re
import sys
import random

badurl = sys.argv[1]
#token = str(random.randint(1, 100000))
#print token
token = '1ABexrukfhIy6dVJYWDxttPsliI5EdBRyW0znpdXdXuwKmjCg6s6KPoZhvMFcrsE'

if "@gmail.com" in badurl:
	print "need to parse " + badurl	    
	raise SystemExit

else:
	print "lets do this"

url = 'http://phishcheck.me/submit/'
referer = 'http://phishcheck.me/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
cookies = {'csrftoken': token, '_ga': '1', '_gid': '1', '_gat': '1'}
payload = {'csrfmiddlewaretoken': token, 'url': badurl, 'useragent': '0'}

# POST with form-encoded data
r = requests.post(url, headers=header, data=payload, cookies=cookies)

# Response, status etc
phishcheckurl = r.url
print phishcheckurl
