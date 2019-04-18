"""
Homework 4
CIS4930
Summer 17
Ryan Winter
rw15e
"""
from __future__ import print_function
import requests, json, re

url1 = "http://imgur.com/user/"
# username here
url2 = "/index/newest/page/"
# number here
url3 = "/hit.json?scrolling"

listPoints = []
listTitle = []
listDate = []
listHash = []

def main_func():
    x = raw_input("Enter username: ")
    #print(x)

    userURL = url1 + x + url2	# holds url with username.. still missing the number and url3
    #print(userURL)

   #for i in xrange(1):
    i = -1
    while True:
	i = i + 1
	fullURL = userURL + str(i) + url3
	
	webpage = requests.get(fullURL)	# saves the page. now source accessible by webpage.text
	#print (webpage.text)		#prints source code of website
	if (webpage.content == ''): 	# exits loop when gets to empty web site
	    break
	#print(i)	# prints counter, to see how many pages crawling through

	if webpage.status_code == 200:	# check if valid url (username is valid)
	    #print ("Valid Username")
            listTitle.append(re.findall('"title":([ a-z A-Z  " ]*)', webpage.text))
	    #listTitle = re.findall('"title":([ a-z A-Z  " ]*)', webpage.text)
       	    #print (listTitle[1])
            listHash.append(re.findall('"hash":([[ a-z A-Z 0-9 " ]*)', webpage.text))
	    #listHash = re.findall('"hash":([[ a-z A-Z 0-9 " ]*)', webpage.text)
	    #print (listHash[1])
            listPoints.append(re.findall('"points":([[ a-z A-Z 0-9 " ]*)', webpage.text))
	    #listPoints = re.findall('"points":([[ a-z A-Z 0-9 " ]*)', webpage.text)
	    #print (listPoints[1])
            listDate.append(re.findall('"datetime":([[ a-z A-Z 0-9- : " ]*)', webpage.text))
	    #listDate = re.findall('"datetime":([[ a-z A-Z 0-9- : " ]*)', webpage.text)
	    #print (listDate[1])

	else:
	    print("Invalid Username")
	    break
    
    highestPoints = 0
    indexOf = 0
    #print("len list points" + str(len(listPoints)))
    for y in xrange(len(listPoints)-1): 				# not currently working..
	if(listPoints[y] > highestPoints):
	    highestPoints = listPoints[y]
	    indexOf = y
	
    #print(highestPoints)
    #print(indexOf)
    #print(listPoints[indexOf])

    #print(listPoints)

    for t in range(6):
	if(t >= 1):
	    print(str(t) + ". " + str(highestPoints))   # + sorted hash
  	    print("Points: ")  # + sorted points
	    print("Title: ")   # + sorted titles
	    print("Date: ")    # + sorted dates

# need to sort them all by highest points value.. listing 1-5 descending order. if a tie, compare hash values
	



# points
# title
# date
# hash









if __name__ == "__main__":
    main_func()
