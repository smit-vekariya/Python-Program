class car:
    __private=10
    model="car100"
    def printcar(self):
        return f"this is {self.model}."

class bike(car):
    model="bike100"
    def printbike(self):
        return f"this is {self.model}."


class bicycal(bike):
    model="by1009"
    def printby(self):
       return f"this is {self.model}."
    


smit=car()
amit=bike()
dmit=bicycal()

# print(smit.private)
print(smit._car__private)
print(dmit.printbike())
print(dmit.printby())
