import json

def func(file):
    with open(file, 'r') as file:
        data = json.load(file)
        out = []
        for i in data:
            if i not in out:
                out.append(i)
    print(out)

func('opem_breweries.json')
