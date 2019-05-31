
import requests
from bs4 import BeautifulSoup

#url="yahoo.com"
url="http://localhost/1/_PHP/_petroblog/"

rsp=requests.get(url)
rsp.status_code

print('STATUS CODE IS ',rsp.status_code)
#print a new line
print()


#print a new line
print()

#print out the raw content of the url or file 
#print(rsp.content)



rsp_src=rsp.content
soup_obj=BeautifulSoup(rsp_src,'lxml')

all_links=soup_obj.find_all("a")


#print(all_links)

'''
**the find_all() method is a soup method which allows us to locate and extract all the a tags in the extracted document 
the result is a list and thus we can apply a for loop as follows
'''
for linkx in all_links:
    print ("---//----")
    print (linkx)
			

	
	
	
	
	
	
	
	
	
	
	
	
	









