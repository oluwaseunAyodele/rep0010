
import requests
from bs4 import BeautifulSoup
from csv import writer
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
#tags = soup_xx.find_all('div', {'class': ['price', 'value']})
dxx = soup_xx.find_all('div', {'class': ['title']})
'''
print( dxx)
print( '\n..........'+'printing line by line'+'...........\n')
for d_xxvalue in dxx:
	print(d_xxvalue)

print( '\n..........'+'printing line by line href attrs  in each '+'...........\n')
with open('posted.csv','w') as csv_file
headers=['Link_Tag','Link_Text','Link_href']

urls = [] 
for a_tag in dxx:
	urls.append(url)
	for elmt in urls:
		print ('href is :','\n',elmt)
	    csv_writer.writerow(elmt)
	
'''		

print( '\n..........'+'printing line by line a tag in each '+'...........\n')
'''	
for a in dxx:
	ahref=a.find('a')
	if (ahref.text):
		a_txt=ahref.text
	else:
		a_txt=''
	print(ahref,'\n',a_txt,'\n',url)
	
	
	
	
#This is a main code block body	
d_divs=soup_obj.findAll('div')
for divx in d_divs:
        # check if the entry is empty or not 
	if divx !="":
	    a_link=divx.findAll('a')
	    for a_x in a_link:
	        print('LINK_TEXT -',a_x.text,'LINK -',a_x )
		    #print(a_x)
	        print('\n'+'-----next div is -----'+'\n')	
	
	
	
	
'''		
	
with open('posted_file.csv','w') as csv_file:
		csv_writer = writer(csv_file)
		headers=['Link_Tag','','Link_Text','','Link_href']
		csv_writer.writerow(headers)	
		for a in dxx:
			ahref=a.find('a')
			try:
				a_txt=ahref.text
				print(ahref,'\n',a_txt,'\n',url)
				towrite_1=[ahref,'\n',a_txt,'\n',url]
				csv_writer.writerow(towrite_1)
			except Exception:
				print(ahref,'\n',url)
				towrite=[ahref,'\n ','\n ','\n',url]
				csv_writer.writerow(towrite)

#Note the '\n' creates the inline empty columns in the final print out
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		