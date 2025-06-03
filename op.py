class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(self.name,"You average is",(sum/3))
student1=student("Ahmed",(33,44,66))
student1.avg()