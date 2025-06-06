class Person:
    def __init__(self ,name ,age):
        self.name=name
        self.age=age
    def Display(self):
        print(f"Name is:{self.name} and age is:{self.age}")
P1=Person("Umair",21)
P1.Display()
P2=Person("Shafahat",20)
P2.Display()
