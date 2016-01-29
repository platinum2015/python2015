'''
 Looks up connections using JSON api at transport.opendata.ch
 Checks 6 large cities in Switzerland
 connections between 16:00 - 19:00.

 Example output:
    Connections leaving from Zurich :
    196 connections using 5 requests with 287.0 estimated capacity.
    
    Connections leaving from Genf :
    21 connections using 1 requests with 27.0 estimated capacity.
    
    Connections leaving from Lausanne :
    33 connections using 1 requests with 65.25 estimated capacity.
    
    Connections leaving from Bern :
    HTTP response seems to be empty
    81 connections using 2 requests with 103.75 estimated capacity.
    
    Connections leaving from Basel :
    37 connections using 1 requests with 60.0 estimated capacity.
    
    Connections leaving from Winterthur :
    72 connections using 2 requests with 104.25 estimated capacity.
    
    I would choose Zurich to start a campaign if I was marketing.


 NOTE: JSON api returns approximately 40 connections,
        at big stations this will not cover three hours.
        In this case additional requests are issued.
'''
import urllib
import json
from datetime import datetime, timedelta, date


api_url = "http://transport.opendata.ch/v1/stationboard"

city_names = ['Zurich', 'Genf','Lausanne', 'Bern', 'Basel','Winterthur']
start_time = "16:00"
nr_of_hours = 3
results = {} #store the result: estimated count of persons per city_name

# create datetime objects for start and stop (three hours later)
start = datetime.combine(date.today(),
                         datetime.strptime(start_time,'%H:%M').time())
stop = start + timedelta(hours=nr_of_hours, minutes=1)


for city_name in city_names:
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
        results[city_name] = 0

        print
        print 'Connections leaving from',city_name,':'

        while not got_one_hour:
            url_values = urllib.urlencode(get_values)
            # if you chose more than one train type
            #for item in transportations:
            #    url_values = url_values + '&transportations[]='+item

            full_url = api_url + "?" + url_values
            response = urllib.urlopen(full_url)
            json_tree = json.loads(response.read())

            if 'stationboard' in json_tree:
                num_requests +=1
                
                all_journeys = json_tree['stationboard']
                
                for journey in all_journeys:
                    dep_time = datetime.strptime(journey['stop']['departure'][:16],'%Y-%m-%dT%H:%M')
                    if dep_time < stop:
                        #use capacity as an estimate for the number of people on board
                        if journey['stop']['prognosis']['capacity1st'] >0:
                            capacity1st = journey['stop']['prognosis']['capacity1st']
                        else:
                            capacity1st = 1
                        if journey['stop']['prognosis']['capacity2nd'] >0:
                            capacity2nd = journey['stop']['prognosis']['capacity2nd']
                        else:
                            capacity2nd = 1
                        #estimate that there are only 1/4 1st class seats
                        results[city_name] += 0.25*capacity1st + 0.75*capacity2nd 
                        count += 1
                        #print '  ',journey['name'],'-to-', journey['to'], ' at', dep_time.strftime('%H:%M')
                    else:
                        got_one_hour = True
                        break
                get_values["datetime"] = (dep_time + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M')
            else:
                print 'HTTP response seems to be empty'
                break
        print count,'connections using',num_requests,'requests with', results[city_name], 'estimated capacity.'

    except Exception, detail:
        print "Couldn't connect to the transport api.", detail

#print the final result (choosen city for campaign)
print
best_city = max(results, key=results.get)
print 'I would choose %s to start a campaign if I was marketing.' %best_city