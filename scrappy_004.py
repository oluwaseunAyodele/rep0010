
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

'''
If we wanted to show only the links that have a specific word in their texts e.g likes

so I want to see all links with the text likes in it


for linkx in all_links:
    print ("---//----")
    if "Likes" in linkx.text: 
        print (linkx)

	
'''	
	
'''		
**the text method , is used to get the text in an extracted data , for example a tag

notice the href attribute in the a tag . we can extract the content of this attribute and print it out.
To do this we modify our forloop as follows 

for linkx in all_links:
    print ("---//----")
    print (linkx)
    print (linkx.text)
    print (linkx.attrs['href'])


OR
'''	





for linkx in all_links:
    print ("---//----")
    print (linkx)	
    print (linkx.attrs['href']+"\n"+linkx.text)
	
	
	
	
	
	
	
	









