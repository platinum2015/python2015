import urllib, json

city_names = ['Zurich', 'Genf','Lausanne', 'Bern', 'Basel','Winterthur']

weather_responses = []

for city in city_names:
    try:
        API_key = "cbf861980e6f74a6da37b86b1b977bc8" #replace with personal key from http://openweathermap.org/appid
        api_url = "http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&APPID=%s" % (urllib.quote(city), API_key)
        response = urllib.urlopen(api_url)
        json_tree = json.loads(response.read())
        weather_responses.append(json_tree)
        if json_tree['cod'] == 200:
            print "added",city
        else:
            print city,"empty?"
    except Exception:
        print "Couldn't connect to the openweathermap service.", city

with open('weather_info.json','w') as my_file:
    json.dump(weather_responses,my_file,indent=4)

##import json
##with open('weather_info.json') as my_file:
##    all_info = json.load(my_file)
##    for city in all_info:
##            print city["name"],city["main"]["temp"]
