import json

x = {
    'first_name' : 'john',
    'last_name' : 'doe',
    'age' : 30
}

my_json = json.dumps(x)

print(my_json)