class car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.price=0 
        
    def printcar(self):
        print(f"{self.name} {self.model} {self.year}")
        
    def carprice(self):
        print(f"car price is {self.price}")
        
    def update_carprice(self,newprice):
        if newprice >=self.price:
            self.price=newprice
        else:
            print("price must incress")
    def increscarprice(self,incresprice):
        self.price+=incresprice
        
class Electroniccar(car):
    def __init__(self,name,model,year):
        super().__init__(name,model,year)
        self.battery=battery()
    
class battery:
    def __init__(self,battery=12):
        self.battery=battery
        
    def printbattery(self):
        print(f"car battery power is {self.battery}")
    def range(self):
        if self.battery==12:
            range=120
        if self.battery >=12:
            range =140
        print("range of car",range)
               
 
        
    
if __name__=="__main__":
   
    myelecar=Electroniccar('BMW','Q11',200)
    myelecar.carprice() 
    myelecar.printcar()
    myelecar.battery.printbattery()
    myelecar.battery.range()
"""
    mycar=car('tata','i10',2011)
    print(mycar.printcar())
    mycar.carprice()
    mycar.price=20
    mycar.carprice()
    mycar.update_carprice(10)
    mycar.carprice()
    mycar.increscarprice(100)
    mycar.carprice()
"""

