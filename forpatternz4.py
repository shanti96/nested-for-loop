n=int(input("enter the row line"))
p=1
for i in range(1,n+1,2):
    for k in range(0,n-i):
        for j in range(p,i+1):
            
for a in range(1,n+1,2):
    for b in range(0,a+1):
        print(" ",end="")
    for c in range(1,n-a):
        print("*",end=" ")     
    print()