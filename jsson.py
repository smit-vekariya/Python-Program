#json= javascrip object notasion\
import json
#json.loads
"""
data='{"name":"smit","age":20}'
parsed=json.loads(data)
print(parsed)
print(parsed['name'])
"""
#json. dumps() function converts a Python object into a json string. 
#dump=convert to javascript its means now its use for javascript also
#What is sort key parameter in dumps?:Use the sort_keys parameter to specify if the result should be sorted or not: json.dumps(x, indent=4, sort_keys=True)
data2={"name":"smit",
       "age":20,
       "car":["ab","bc"],
       "isbad":False
    } 
jscomp=json.dumps(data2, indent=4, sort_keys=True)
print(jscomp)