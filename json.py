import json

def func(file):
    with open(file, 'r') as file:
        data = json.load(file)
        for i in data:
            if(i['state'] == 'delhi') or (i['state'] == 'bihar'):
                print(i['office_name'])
                print(i['pincode'])

func('india.json')
