
import requests
from bs4 import BeautifulSoup

#url="yahoo.com"
url="http://localhost/1/_PHP/_petroblog/"

rsp=requests.get(url)
rsp.status_code

print('STATUS CODE IS ',rsp.status_code)
print()
print (rsp.headers)

			

	
	
	
	
	
	
	
	
	
	
	
	
	









