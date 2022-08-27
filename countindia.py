import json

def func(file):
    with open(file, 'r') as file:
        data = json.load(file)
        a = 0
        for i in data:
            a = a+1
        print(a)

func('india.json')
