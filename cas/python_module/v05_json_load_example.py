import json

#ignore the "def" block as long as you don't know functions
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


json_as_text = '''
{
    "Name": "McGregor",
    "Firstname": "John",
    "Points": [100, 90, 85]
}

'''
print type(json_as_text)
print json_as_text

info = json.loads(json_as_text)
print type(info)
print info
print convert(info)
