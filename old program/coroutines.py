import time
from typing import Text

def sercher():
    book="my name is smit and i want to learn python and django."
    time.sleep(2)

    while True:
        Text=(yield)
        if Text in book:
            print("yes")
        else:
            print("no")

s=sercher()
serch=input("Enter word for serching:")
print("Start searching....")
s.__next__()
#next(s)
s.send(serch)




"""
s=sercher()
E=input("Enter your text:")
print("searching...")
s.__next__()
s.send(E)
"""




    