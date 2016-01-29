weather_responses = '''
[
    {
        "clouds": {
            "all": 36
        }, 
        "name": "Zurich", 
        "coord": {
            "lat": 47.37, 
            "lon": 8.55
        }, 
        "sys": {
            "country": "CH", 
            "message": 0.0034, 
            "sunset": 1445703700, 
            "sunrise": 1445666249
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 802, 
                "icon": "03d", 
                "description": "scattered clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1445693575, 
        "main": {
            "temp": 14.01, 
            "grnd_level": 968.74, 
            "temp_max": 14.01, 
            "sea_level": 1032.66, 
            "humidity": 92, 
            "pressure": 968.74, 
            "temp_min": 14.01
        }, 
        "id": 2657896, 
        "wind": {
            "speed": 1.17, 
            "deg": 173.502
        }
    }, 
    {
        "clouds": {
            "all": 44
        }, 
        "name": "Gen\u00e8ve", 
        "coord": {
            "lat": 46.21, 
            "lon": 6.14
        }, 
        "sys": {
            "country": "CH", 
            "message": 0.0029, 
            "sunset": 1445704397, 
            "sunrise": 1445666711
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 802, 
                "icon": "03d", 
                "description": "scattered clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1445696584, 
        "main": {
            "temp": 12.81, 
            "grnd_level": 947.26, 
            "temp_max": 12.81, 
            "sea_level": 1033.11, 
            "humidity": 83, 
            "pressure": 947.26, 
            "temp_min": 12.81
        }, 
        "id": 7285902, 
        "wind": {
            "speed": 1.02, 
            "deg": 211.002
        }
    }, 
    {
        "clouds": {
            "all": 0
        }, 
        "name": "Lausanne", 
        "visibility": 10000, 
        "sys": {
            "country": "CH", 
            "sunset": 1445704247, 
            "message": 0.0293, 
            "type": 1, 
            "id": 6002, 
            "sunrise": 1445666625
        }, 
        "weather": [
            {
                "main": "Clear", 
                "id": 800, 
                "icon": "01d", 
                "description": "Sky is Clear"
            }
        ], 
        "coord": {
            "lat": 46.52, 
            "lon": 6.63
        }, 
        "base": "stations", 
        "dt": 1445696400, 
        "main": {
            "pressure": 1020, 
            "temp_min": 14, 
            "temp_max": 17, 
            "temp": 15.78, 
            "humidity": 67
        }, 
        "id": 2659994, 
        "wind": {
            "speed": 1
        }, 
        "cod": 200
    }, 
    {
        "clouds": {
            "all": 0
        }, 
        "name": "Bern", 
        "visibility": 10000, 
        "sys": {
            "country": "CH", 
            "sunset": 1445704005, 
            "message": 0.0405, 
            "type": 1, 
            "id": 6013, 
            "sunrise": 1445666472
        }, 
        "weather": [
            {
                "main": "Clear", 
                "id": 800, 
                "icon": "01d", 
                "description": "Sky is Clear"
            }
        ], 
        "coord": {
            "lat": 46.95, 
            "lon": 7.45
        }, 
        "base": "stations", 
        "dt": 1445696400, 
        "main": {
            "pressure": 1019, 
            "temp_min": 14, 
            "temp_max": 15, 
            "temp": 14.5, 
            "humidity": 72
        }, 
        "id": 2661552, 
        "wind": {
            "speed": 2.1, 
            "deg": 150
        }, 
        "cod": 200
    }, 
    {
        "clouds": {
            "all": 0
        }, 
        "name": "Basel", 
        "visibility": 10000, 
        "sys": {
            "country": "CH", 
            "sunset": 1445703911, 
            "message": 0.039, 
            "type": 1, 
            "id": 5646, 
            "sunrise": 1445666508
        }, 
        "weather": [
            {
                "main": "Clear", 
                "id": 800, 
                "icon": "01d", 
                "description": "Sky is Clear"
            }
        ], 
        "coord": {
            "lat": 47.56, 
            "lon": 7.57
        }, 
        "base": "stations", 
        "dt": 1445696400, 
        "main": {
            "pressure": 1018, 
            "temp_min": 14, 
            "temp_max": 18, 
            "temp": 15.91, 
            "humidity": 59
        }, 
        "id": 2661604, 
        "wind": {
            "speed": 1
        }, 
        "cod": 200
    }, 
    {
        "clouds": {
            "all": 36
        }, 
        "name": "Winterthur", 
        "coord": {
            "lat": 47.5, 
            "lon": 8.75
        }, 
        "sys": {
            "country": "CH", 
            "message": 0.0029, 
            "sunset": 1445703635, 
            "sunrise": 1445666218
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 802, 
                "icon": "03d", 
                "description": "scattered clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1445696249, 
        "main": {
            "temp": 14.01, 
            "grnd_level": 968.74, 
            "temp_max": 14.01, 
            "sea_level": 1032.66, 
            "humidity": 92, 
            "pressure": 968.74, 
            "temp_min": 14.01
        }, 
        "id": 2657970, 
        "wind": {
            "speed": 1.17, 
            "deg": 173.502
        }
    }
]
'''
# Start your code here
import json
all_info = json.loads(weather_responses)
city_names = []
temperatures = []
pressures = []
humidities = []
raining_cities = []
cloudy_cities = []


for city in all_info:
    
    city_names.append(city["name"])
    temperatures.append(city["main"]["temp"])
    pressures.append(city["main"]["pressure"])
    humidities.append(city["main"]["humidity"])
    
    print city_names[-1],":",temperatures[-1],"deg,",pressures[-1],"bar,",humidities[-1],"%"

    if "broken cloud" in city["weather"][0]["description"]:
        cloudy_cities.append(city["name"])
    if "rain" in city["weather"][0]["description"]:
        raining_cities.append(city["name"])

print
print "Warmest in", city_names[temperatures.index(max(temperatures))],
print "with", max(temperatures) , "degrees"

print "Highest humidity in", city_names[humidities.index(max(humidities))],
print "with", max(humidities) , "%"

print "Highest pressure in", city_names[pressures.index(max(pressures))],
print "with", max(pressures) , "bar"

print
print "It is raining in",len(raining_cities),"cities"
for c in raining_cities: print c,

print
print "Broken clouds in",len(cloudy_cities),"cities"
for c in cloudy_cities: print c,
