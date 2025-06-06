list=[0,0,0,0,0]
for i in range(5):
    list[i]=int(input(f"Enter {i+1}th number:"))
list.sort()
print("Smallest number in list is:"+str(list[0]))
print("Largest number in the list is:"+str(list[4]))
sum=0
for i in list:
    sum+=i
print("The sum is:"+str(sum))
print("The Average is:"+str(sum/5))