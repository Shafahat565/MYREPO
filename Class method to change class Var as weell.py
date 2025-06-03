#direct value aos8 chang3 in class also
class person:
    name="anonymous "
    def changename(self,name):
        self.name=name

P1=person()
P1.changename("Hamza")
print(P1.name)
#masla ka class ma anonymous not changed 
print(person.name)
#now solution 
class persen:
    name="anonys "
    @classmethod
    def cangename(cls,name):
        cls.name=name 
 #ya pir persen.name=name
 #ya pir self.__class__.namname=name
P2=persen()
P2.cangename("Hamza")
print(P2.name)
print(persen.name)
