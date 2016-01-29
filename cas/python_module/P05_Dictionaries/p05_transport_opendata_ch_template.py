'''
 Looks up connections using JSON api at transport.opendata.ch
 Provide a city name and a start time
 connections within the start time plus one hour are provided.

 NOTE: JSON api returns approximately 40 connections,
        at big stations this will not cover an entire hour.
        In this case additional requests are issued to fill one hour.
'''
import urllib
import json
from datetime import datetime, timedelta, date

#
api_url = "http://transport.opendata.ch/v1/stationboard"

# User input
city_name = raw_input("Looking up trains. Which city? ")
start_time = raw_input("What time? Type like 22:30 ")

# create datetime objects for start and stop (one hour later)
start = datetime.combine(date.today(),
                         datetime.strptime(start_time,'%H:%M').time())
stop = start + timedelta(hours=1,minutes=1)


# Prepare http get variables as dictionary
get_values = {}
get_values["station"] = city_name
get_values["datetime"] = start.strftime('%Y-%m-%d %H:%M')#start time
get_values["transportations[]"] = 's_sn_r'# just get the s-bahn

# Do this if you want more than one type of train
#transportations = [ 'ice_tgv_rj', 'ec_ic', 'ir', 're_d', 's_sn_r']


# Do the work
try:
    got_one_hour = False
    num_requests = 0
    count = 0
    
    print 'Connections leaving from',city_name
    print 'between',start.strftime('%H:%M'),"and",stop.strftime('%H:%M')

    while not got_one_hour:
        url_values = urllib.urlencode(get_values)
        # if you chose more than one train type
        #for item in transportations:
        #    url_values = url_values + '&transportations[]='+item

        full_url = api_url + "?" + url_values

        #debug only
        #print full_url

        response = urllib.urlopen(full_url)
        json_tree = json.loads(response.read())

        if 'stationboard' in json_tree:
            num_requests +=1
            
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
        else:
            print 'HTTP response seems to be empty'
            break
    print 'found',count,'connections using',num_requests,'requests'

except Exception, detail:
    print "Couldn't connect to the transport api.", detail
