# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:23:55 2015

@author: programming
"""
print("Hello"+" World. "+ "repeat_"*5)
word="abcdefg"
i=3
print( word[:i]+word[i]+word[i+1:])
print(len(word))

print("word.find(\"d\"): %r" % word.find("d"))
word="apples,bananas,tomatoes"
print("word.find(\"d\"): %r" % word.find("an"))
print(word.split(","))
sp=word.split(",")
print(type(sp))


import urllib,json
city_name= raw_input("What city would you like to know about? ")
API_key= "77028127b3488cd86df47953d28bd086"
x= (urllib.quote(city_name), API_key)
api_url= "http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&APPID=%s" % (urllib.quote(city_name), API_key)
print(api_url)
try: 
    print(api_url)
    response = urllib.urlopen(api_url)
    json_tree= json.loads(response.read())

    if json_tree['cod'] == 200:
        temperature = json_tree["main"]["temp"]
        description = json_tree["weather"][0]["description"]
    
        print "It is " + str(temperature) +  " degrees in " + city_name
        print "The weather can be described as \"" + description + "\"."
        print (type(response))        
    else:
        print "The service doesn't know that city."
except Exception:
    print "Couldn't connect to the openweathermapservice."
"""
{
"coord":
     {"lon":6.63,"lat":46.52},
"weather":[
          {"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}
          ],
"base":"stations",
"main":
    {"temp":10.23,"pressure":1018,"humidity":62,"temp_min":6,"temp_max":13},
"visibility":10000,
"wind":    {"speed":5.1,"deg":60},
"clouds":{"all":40},
"dt":1445266200,
 "sys":
        {"type":1,"id":6010,"message":0.0107,"country":"CH","sunrise":1445234204,"sunset":1445272757},
"id":2659994,
"name":"Lausanne",
"cod":200
 }

"""


choice=int(raw_input("think a number between 1 and 10"))
question="was it  %i? y/n"
if raw_input("was it  5? y/n") == "y":
    if raw_input("was it  Greater than  8? y/n")  == "y":
        if raw_input("was it  Greater than  9? y/n") =="y":
            if raw_input("was it  9? y/n") =="y" :
                print ("found 9! %i" % choice) 
            else:
                print ("found 10! %i" % choice)
        else:
            print  ("found 8! %i" % choice)   
    else:
          if raw_input("was it  Greater than  6? y/n") =="y":
            if raw_input("was it  6? y/n") =="y" :
                print ("found 6! %i" % choice) 
            else:
                print ("found 7! %i" % choice)
          else:
            print  ("found 5! %i" % choice)                
else:
    if raw_input("was it  Greater than  3? y/n")  == "y":
        if raw_input("was it  Greater than  4? y/n") =="y":
            if raw_input("was it  4? y/n") =="y" :
                print ("found 4! %i" % choice) 
            else:
                print ("found 5! %i" % choice)
        else:
            print  ("found 3! %i" % choice)   
    else:
          if raw_input("was it  2? y/n") =="y":
              print ("found 2! %i" % choice)
          else:
              print  ("found 1! %i" % choice) 
