import urllib

API_key = "cbf861980e6f74a6da37b86b1b977bc8" #replace with personal key from http://openweathermap.org/appid
api_url= "http://api.openweathermap.org/data/2.5/weather"

get_values = {"units":"metric", "q":"Zurich", "APPID":API_key}
url_values = urllib.urlencode(get_values)

full_url = api_url + '?' + url_values

print full_url

try: 
    response = urllib.urlopen(full_url)
except Exception:
    print "Couldn't connect to the openweathermap service.", full_url
else:
    print response.read()
