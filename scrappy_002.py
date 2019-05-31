
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



#The prettify() can be used to display output in a well formatted pattern
#print(soup_obj.prettify())


#This will print the first occurence of the p tag in the document if none exists it will print None
#print(soup_obj.p)

#This will print the first occurence of the b tag in the document if none exists it will print None
#print(soup_obj.b)

#This will print all the occurences of the b tag in the document if none exists it will print an empty list. The findAll method returns a list

print(soup_obj.find_all('b'))

			

	
	
	
	
	
	
	
	
	
	
	
	
	









