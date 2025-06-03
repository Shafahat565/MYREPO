class Vehicles:
    Vack="Hello vechicle"
    
class Car(Vehicles):
    Came="Car"
    def __init__(self,type):
        self.type=type
        
class Bus(Car):
    Bame="Bus"
    def __init_(self,cal):
        self.loc=cal
        
class vego:
    vegome="vego"  
          
class toyota(Car,vego):
    def __init__(self,name):
        self.name=name
   
#single inherirence      
Class1=Car("Racecar")
print(Class1.type,Class1.Vack)

#mulilevel inheritence
Class2=Bus("Localha")
print(Class2.Bame,Class2.Vack,Class2.Came)

#multiple inhesitance
Class3=toyota("Toyo")
print(Class3.vegome,Class3.Came,Class3.Vack,Class3.name)