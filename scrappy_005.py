
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
soup_xx=BeautifulSoup(rsp_src,'lxml')
#print(soup_obj)
'''

'''	


#tags = soup_xx.find_all('div', {'class': ['price', 'value']})
dxx = soup_xx.find_all('div', {'class': ['title']})

print( dxx)
print( '\n..........'+'printing line by line'+'...........\n')
for d_xxvalue in dxx:
	print(d_xxvalue)


print( '\n..........'+'printing line by line a tag in each '+'...........\n')

for a in dxx:
	ahref=a.find('a')
	print(ahref)


print( '\n..........'+'printing line by line href attrs  in each '+'...........\n')


urls = [] 
for a_tag in dxx:
	urls.append(url)
	for elmt in urls:
		print ('href is :','\n',elmt)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
