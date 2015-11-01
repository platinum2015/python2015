# -*- coding: utf-8 -*-
import urllib
import json
from datetime import datetime, timedelta, date
api_url = "http://transport.opendata.ch/v1/stationboard"
api_url = "http://transport.opendata.ch/v1/locations"

get_values = {}
get_values["query"] = "Horg"
try:
    url_values = urllib.urlencode(get_values)
    full_url = api_url + "?" + url_values
    print full_url

    response = urllib.urlopen(full_url)
    json_tree = json.loads(response.read())
#    print(json_tree)
    if 'stations' in json_tree:
        print(json_tree["stations"][0]["name"])
        """    num_requests +=1
            
            all_journeys = json_tree['stationboard']
            
            for journey in all_journeys:
                dep_time = datetime.strptime(journey['stop']['departure'][:16],'%Y-%m-%dT%H:%M')
                if dep_time < stop:
                    count +=1
                    print '  ',journey['name'],'-to-', journey['to'], ' at', dep_time.strftime('%H:%M')
                else:
                    got_one_hour = True
                    break
            get_values["datetime"] = (dep_time + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M')
            """
        pass
    else:
        print 'HTTP response seems to be empty'
except Exception, detail:
    print "Couldn't connect to the transport api.", detail

