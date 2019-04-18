"""
Homework 4
CIS4930
Summer 17
Ryan Winter
rw15e
"""
from __future__ import print_function
import requests, json

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

    i = -1
    while True:
	i = i + 1	# counts how many times loop runs (how many pages looped through)
	fullURL = userURL + str(i) + url3 # constructs the full url based on user input and while loop
	webpage = requests.get(fullURL)	# saves the page. now source accessible by webpage.text
        
     
        try:
            data = json.loads(webpage.text)
	except:
            pass
        #print(data)

	if (webpage.content == ''): 	# exits loop when gets to empty web site(the last page of comments)
	    break
	#print(i)	# prints counter, to see how many pages crawling through

	if webpage.status_code == 200:	# check if valid url (username is valid)
	    #print ("Valid Username")
            try:
                for z in xrange(20):
                    listHash.append(data['data']['captions']['data'][z]['hash'])
                    listPoints.append(data['data']['captions']['data'][z]['points'])
                    listTitle.append(data['data']['captions']['data'][z]['title'])
                    listDate.append(data['data']['captions']['data'][z]['datetime'])
            except: 
                pass

            #break # REMOVE AFTER TESTING

	else:
	    print("Invalid Username")
	    #break
            exit()
           
    highestPoints1 = 0
    highestPoints2 = 0
    highestPoints3 = 0
    highestPoints4 = 0
    highestPoints5 = 0
    indexOf1 = 0
    indexOf2 = 0 
    indexOf3 = 0
    indexOf4 = 0
    indexOf5 = 0
    #print("length of listPoints " + str(len(listPoints)))
    for y in xrange(len(listPoints)): 				# ugly sorting...
	if(listPoints[y] > highestPoints1):
	    highestPoints1 = listPoints[y]
	    indexOf1 = y
        elif(listPoints[y] == highestPoints1):
            indexOf2 = y # if listpoints hp1 are same, set hp2 to this same value..
	if(listPoints[y] < highestPoints1):
            if(listPoints[y] > highestPoints2):
                highestPoints2 = listPoints[y]
                indexOf2 = y
                if(listPoints[y] == highestPoints2):
                    indexOf3 = y # if listpoints hp2 are same, set hp3 to this same value..
        if(listPoints[y] < highestPoints2):
            if(listPoints[y] > highestPoints3):
                highestPoints3 = listPoints[y]
                indexOf3 = y
                if(listPoints[y] == highestPoints3):
                    indexOf4 = y # if listpoints hp3 are same, set hp4 to this same value..
        if(listPoints[y] < highestPoints3):
            if(listPoints[y] > highestPoints4):
                highestPoints4 = listPoints[y]
                indexOf4 = y
                if(listPoints[y] == highestPoints4):
                    indexOf5 = y # if listpoints hp4 are same, set hp5 to this same value..
        if(listPoints[y] < highestPoints4):
            if(listPoints[y] > highestPoints5):
                highestPoints5 = listPoints[y]
                indexOf5 = y
    #print(highestPoints1)
    #print(indexOf1)

    #if(highestPoints1 == highestPoints2):
     #       if(listHash[indexOf1] > listHash[indexOf2]):
                #print indexOf1 first
      #      else:
                #print indexOf2 first
 
    print("1. " + str(listHash[indexOf1]))    # + sorted hash
    print("Points: " + str(listPoints[indexOf1]))  # + sorted points
    print("Title: " + listTitle[indexOf1])   # + sorted titles
    print("Date: "+ str(listDate[indexOf1]))    # + sorted dates

    print("2. " + str(listHash[indexOf2]))    # + sorted hash
    print("Points: " + str(listPoints[indexOf2]))  # + sorted points
    print("Title: " + listTitle[indexOf2])   # + sorted titles
    print("Date: "+ str(listDate[indexOf2]))    # + sorted dates

    print("3. " + str(listHash[indexOf3]))    # + sorted hash
    print("Points: " + str(listPoints[indexOf3]))  # + sorted points
    print("Title: " + listTitle[indexOf3])   # + sorted titles
    print("Date: "+ str(listDate[indexOf3]))    # + sorted dates

    print("4. " + str(listHash[indexOf4]))    # + sorted hash
    print("Points: " + str(listPoints[indexOf4]))  # + sorted points
    print("Title: " + listTitle[indexOf4])   # + sorted titles
    print("Date: "+ str(listDate[indexOf4]))    # + sorted dates

    print("5. " + str(listHash[indexOf5]))    # + sorted hash
    print("Points: " + str(listPoints[indexOf5]))  # + sorted points
    print("Title: " + listTitle[indexOf5])   # + sorted titles
    print("Date: "+ str(listDate[indexOf5]))    # + sorted dates


    #for t in range(6):
	#if(t >= 1):
	    #print(str(t) + ". ")    # + sorted hash
  	    #print("Points: ")  # + sorted points
	    #print("Title: ")   # + sorted titles
	    #print("Date: ")    # + sorted dates

if __name__ == "__main__":
    main_func()
