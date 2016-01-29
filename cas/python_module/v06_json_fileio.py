import json

a_dict ={"Name": "McGregor","Firstname": "John","Points": [100, 90, 85]}

json_file = open('test_json.txt','w')
json.dump(a_dict,json_file,indent=4)
json_file.close()


json_file = open('test_json.txt','r')
a_dict_loaded = json.load(json_file)

json_file.seek(0)
json_as_string = json_file.read()

json_file.close()

print a_dict
print 'Written to file:'
print json_as_string
print 'Reloaded into dict'
print a_dict_loaded
