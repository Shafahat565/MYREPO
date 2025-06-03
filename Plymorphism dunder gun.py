class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary 
    def showNum(self):
        print(self.real,"i+",self.imaginary,"j")
    def __add__(self,num2):
        real1=self.real+num2.real
        img1=self.imaginary+num2.imaginary
        return Complex(real1,img1)
num1=Complex(3,4)
num1.showNum()       
num2=Complex(4,12)
num2.showNum()
num3=num2.__add__(num1)
num3.showNum()
num3=num1+num2
num3.showNum()        