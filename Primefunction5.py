def primecheck(A):
    if  A==2 or A==3:
        print (f"{A} is prime number.")
        return
    elif  A==0 or A==1:
        print (f"{A} is not a prime number.")
        return
    check=0
    for j in range (int(A/2+1)):
        if A%(j+2)==0:
            check=1
    if check==0:
        print (f"{A} is prime number.")
    else:
        print (f"{A} is not a prime number.")
for i in range(50):
    primecheck(i)

        
