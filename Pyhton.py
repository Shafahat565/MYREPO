x=5
if x>5:
    print(f"{x} is greater than 5.")
else:
    print(f"{x} is Lesser than 5.")
x=10
if x>5:
    print(f"{x} is greater than 5.")
else:
    print(f"{x} is Lesser than 5.")
print("Loop Printing")
for i in range(5):
    print(i)
print("List elemenst printing")
List=[1,2,3,4,5,6,7,8,9]
for g in List:
    print(g)
print("Tuple printing")
tuple=(1,2,3,4,5,6)
for k in tuple:
        print(k)
print("While loop printing")
y=12
while y<15:
    print(y)
    y+=1
def PrintName(name):
    return "Hello "+name
print(PrintName("Shafahat Nisar"))
def square(x):
    return x*x
print(square(33333333313123123213122322333))
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def printff(self):
        print("Name: " + self.name + "\nRoll No: " + str(self.roll_no))

Student1 = Student("Umair", 111)
Student1.printff()
