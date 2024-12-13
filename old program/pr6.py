
"""
import re
strr="my name is smit"
x=re.search("name",strr)
print(x.string)
print(x.span())
print(x.group())
"""
import camelcase
c=camelcase.CamelCase()
txt="this is python file."
print(c.hump(txt))