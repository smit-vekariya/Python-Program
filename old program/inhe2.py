class dad:
    basketball=1

class son(dad):
    dance=1
    def printson(self):
        return f"i can {self.dance} type o dance. "

class grand(son):
    dance=2
    # def printson(self):
    #    return f"i can {self.dance} type of dance"


nikunj=dad()
smit=son()
gecson=grand()

print(gecson.printson())
gal=smit.basketball
print(gal)
print(gecson.basketball)