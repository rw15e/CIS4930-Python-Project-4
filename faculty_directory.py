"""
Homework 4 
CIS4930
Summer 17
Ryan Winter
rw15e
"""

from __future__ import print_function
import requests, lxml, sys, re

url = "http://www.cs.fsu.edu/department/faculty"

def get_info():
    main_page = requests.get(url)
    link = re.findall('<td style="text-align: center;"><a href="?\'?([^"\'>]*)', main_page.text)
    #print(link[1])		# This works, stores all 35 specific urls in a list

    if link:
	#print("Test")
	page2 = [None]*50
	for x in range(len(link)):
	    page2[x] = (requests.get(link[x]))		# this sets the list page2 to hold the source code 
	    #print (page2[x].text)	# this prints the source code of all 35 webpages
    else:
	return None

# need to loop through page2 and scrape the name, office, phone #, and email and print them all to the user
    name = [None] * len(page2)
    office = [None] * len(page2)
    phone = [None] * len(page2)
    email = [None] * len(page2)
    for i in range(len(page2)-15):
        name[i] = re.findall(r'<title>([a-z-A-z . "\</title>]*)', page2[i].text) 
	print ("Name: " + str(name[i][0]))

	office[i] = re.findall(r'<td>([0-9 a-zA-Z "]*)', page2[i].text)        
	if(office[i]):    
	    if(office[i][1]):
	        print("Office: " + str(office[i][1]))
   	    else:
	        print("Office: N/A")
	else:
	    print("Office: N/A")

  	phone[i] = re.findall(r'<td>([(0-9) - -0-9 "]*)', page2[i].text)  	
	if(phone[i]): 	
	    if(phone[i][3]):
	        print("Telephone: " + str(phone[i][3]))
   	    else:
                print("Telephone: N/A")

	email[i] = re.findall(r'<td>([[ a-z A-Z  " ]*)', page2[i].text)
	if(email[i]): 	
	    if(email[i][4]):
	    	print("E-Mail: " + str(email[i][4]) + " ]")
   	    else:
            	print("E-Mail: N/A")
	else:
		print("E-Mail: N/A")
	print("****************************************")

if __name__ == "__main__":
    get_info()
