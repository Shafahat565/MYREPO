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
