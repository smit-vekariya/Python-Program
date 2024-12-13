import requests
p=requests.get("https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=YOUR_API_KEY") #its works
print(p.text)
print(p.status_code)
# in video 81 and find in gootgle for more post method in requests
"""
url="www.sometings.com"
data_of_url={
    "p1":4,
    "p2":5
}
r2=requests.post(url,data=data_of_url)
print(r2)
"""