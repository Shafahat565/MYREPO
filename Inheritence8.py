class Animal:
    def __init__(self, name):  
        self.name = name

    def sound(self):          
        print("Animal Speaks")


class Dog(Animal):
    def __init__(self, name):  
        super().__init__(name) 

    def sound(self):
        print("Bark.")


Dog1 = Dog("Duffy")  
print(f"The name is {Dog1.name} and sound is: ", end="")
Dog1.sound()