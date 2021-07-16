import json

data = {
    "sites": ["cricbuzz.com", "espncricenfo.com"],
    "wtc_finalist": ['india','newzeland'],
    "ground": ('Ages Bowl', 'Southamptan')
}

jscomp = json.dumps(data)
print(jscomp)

data2 = '{"var1":"cricket", "var2":18}'
parsed = json.loads(data2)
print(parsed)