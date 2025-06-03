for i in range(9,0,-1):
    for j in range(0,i,1):
        print(i*j," ",end='')
    print("\n")   
    
for i in range(0,9,1):
    for j in range(i,0,-1):
        print(i*j," ",end='')
    print("\n")
for i in range(0,5,1):
    for j in range(5,i,-1):
        print(" ",end='')
    for k in range(2*i-1,0,-1):
        print("*",end='')    
    print("")        
    