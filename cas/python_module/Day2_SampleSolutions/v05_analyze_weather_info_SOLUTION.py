weather_responses = '''
[
    {
        "clouds": {
            "all": 90
        }, 
        "name": "Zurich", 
        "coord": {
            "lat": 47.37, 
            "lon": 8.55
        }, 
        "sys": {
            "country": "CH", 
            "sunset": 1417707376, 
            "message": 0.1971, 
            "type": 1, 
            "id": 6007, 
            "sunrise": 1417676164
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 804, 
                "icon": "04n", 
                "description": "overcast clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1417726789, 
        "main": {
            "pressure": 1014, 
            "temp_min": 4, 
            "temp_max": 5, 
            "temp": 4.4, 
            "humidity": 86
        }, 
        "id": 2657896, 
        "wind": {
            "speed": 1.32, 
            "deg": 47.5016
        }
    }, 
    {
        "clouds": {
            "all": 90
        }, 
        "name": "Geneva", 
        "coord": {
            "lat": 46.21, 
            "lon": 6.14
        }, 
        "sys": {
            "country": "Switzerland", 
            "sunset": 1417708213, 
            "message": 0.1879, 
            "type": 1, 
            "id": 6002, 
            "sunrise": 1417676482
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 804, 
                "icon": "04n", 
                "description": "overcast clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1417726200, 
        "main": {
            "pressure": 1014, 
            "temp_min": 5, 
            "temp_max": 7, 
            "temp": 5.97, 
            "humidity": 87
        }, 
        "id": 7285902, 
        "wind": {
            "speed": 0.5, 
            "deg": 0
        }
    }, 
    {
        "clouds": {
            "all": 90
        }, 
        "name": "Lausanne", 
        "coord": {
            "lat": 46.52, 
            "lon": 6.63
        }, 
        "sys": {
            "country": "CH", 
            "sunset": 1417708028, 
            "message": 0.0969, 
            "type": 1, 
            "id": 6010, 
            "sunrise": 1417676432
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 804, 
                "icon": "04n", 
                "description": "overcast clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1417726496, 
        "main": {
            "pressure": 1014, 
            "temp_min": 2.3, 
            "temp_max": 6, 
            "temp": 4.46, 
            "humidity": 93
        }, 
        "id": 2659994, 
        "wind": {
            "speed": 1, 
            "deg": 0
        }
    }, 
    {
        "clouds": {
            "all": 90
        }, 
        "name": "Bern", 
        "coord": {
            "lat": 46.95, 
            "lon": 7.45
        }, 
        "sys": {
            "country": "CH", 
            "sunset": 1417707736, 
            "message": 0.0954, 
            "type": 1, 
            "id": 6013, 
            "sunrise": 1417676333
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 804, 
                "icon": "04n", 
                "description": "overcast clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1417724400, 
        "main": {
            "pressure": 1014, 
            "temp_min": 4, 
            "temp_max": 5, 
            "temp": 4.39, 
            "humidity": 93
        }, 
        "id": 2661552, 
        "wind": {
            "speed": 1.5, 
            "deg": 0
        }
    }, 
    {
        "clouds": {
            "all": 75
        }, 
        "name": "Basel", 
        "coord": {
            "lat": 47.56, 
            "lon": 7.57
        }, 
        "sys": {
            "country": "CH", 
            "sunset": 1417707566, 
            "message": 0.0331, 
            "type": 1, 
            "id": 5646, 
            "sunrise": 1417676443
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 803, 
                "icon": "04n", 
                "description": "broken clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1417725889, 
        "main": {
            "pressure": 1015, 
            "temp_min": 4, 
            "temp_max": 4, 
            "temp": 4, 
            "humidity": 93
        }, 
        "id": 2661604, 
        "wind": {
            "speed": 1.5, 
            "deg": 290
        }
    }, 
    {
        "clouds": {
            "all": 90
        }, 
        "name": "Winterthur", 
        "coord": {
            "lat": 47.5, 
            "lon": 8.75
        }, 
        "sys": {
            "country": "CH", 
            "sunset": 1417707297, 
            "message": 0.1803, 
            "type": 3, 
            "id": 6007, 
            "sunrise": 1417676146
        }, 
        "weather": [
            {
                "main": "Clouds", 
                "id": 804, 
                "icon": "04n", 
                "description": "overcast clouds"
            }
        ], 
        "cod": 200, 
        "base": "cmc stations", 
        "dt": 1417727087, 
        "main": {
            "pressure": 1015, 
            "temp_min": 3.7, 
            "temp_max": 4.5, 
            "temp": 4.0700000000001, 
            "humidity": 86
        }, 
        "id": 2657970, 
        "wind": {
            "speed": 1.32, 
            "deg": 47.5016
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
