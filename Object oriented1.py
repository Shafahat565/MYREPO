College="Cui"
class comsats:
    def __init__(self,name,program,marks):
        self.name=name
        self.program=program
        self.marks=marks
        self.dict={
            "collgeName":College,
            "studentName":self.name,
            "studentProgram":self.program,
            "studentMarks":self.marks
            }
class School: 
    name="Almeezan" 
class Math:
    def sum(self,a,b):
      return a+b    
    def subtract(self,a,b):
      return a-b  
    def multi(self,a,b):
      return a*b     
    def div(self,a,b):
      return a//b   
    def palindrome(self,a):
        result=0
        while(a>0):
            remainder=a%10
            result=result*10+remainder
            a//=10
        return result 
    def oct(self,a):
        result=0
        count=1
        while(a>0):
           remainder=a%2
           result=remainder*count+result
           count*=10
           a//=2
        return result    
student1=comsats("Anas","Bcs",82)
print("Date of 1=",student1.dict)
Schooling=School()
print(Schooling.name)
print(student1.dict.values())
print(list(student1.dict.keys()))
submission=Math()
print(submission.palindrome(536))
print(submission.div(20,2))
print(submission.oct(10))