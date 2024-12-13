#code with harry website all code are there for refrence
import re
mystr='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +919537127284
mo: +919712814409
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaii'''

#patt=re.compile(r'tata')
#patt=re.compile(r'\d{5}-\d{4}')
# Given a string with a lot of indian phone numbers starting from +91
patt=re.compile(r'\+91\d{10}\b')
finds=patt.finditer(mystr)
for find in finds:
    print(find)