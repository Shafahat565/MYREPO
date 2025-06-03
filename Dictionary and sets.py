dictionary={ 
    "Name":"Amjad",
    "Class":3,
    "Major":"CS",
    "Subjects":{
        "ICT":24 ,
        "PF":25 ,
        "oop":34
        }
}
print("Main dictionary is:",dictionary,"\n")
print("pf marks are",dictionary["Subjects"]["PF"],"\n")
print("keys are :",dictionary.keys(),"\n")
print("values are :",dictionary.values(),"\n")
listi=list(dictionary.items())
print("items in list as tuple are",listi,"\n")
print('Subject .')
print(dictionary.get("Subjects"),"\n")
new={1:1}
dictionary.update(new)
print("New dictionary is",dictionary,"\n")

set={1,3,5,7,9}
print("set is =",set)
set.add(12)
print("set after add 12 is =",set)
set.remove(1)
print("set after removing 1 is =",set)
set.pop()
print("Random pop",set)
set.clear()
print("Set moye moye=",set)

A={1,2,3,4,5,6,7,8}
B={4,5,6,7,8,9,10,11,12}
print("AUB is=",A.union(B))
print("AnB is=",A.intersection(B))
print(list(A))
