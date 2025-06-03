class Test:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.math = sub1
        self.phy = sub2
        self.comp = sub3
        
    @property
    def avg(self):
         print((self.math + self.phy + self.comp) / 3)

student = Test("Saghir", 33, 45, 64)
student.avg
student.math=48
student.avg