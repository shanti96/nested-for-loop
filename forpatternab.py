n=int(input("enter the number"))
p=1
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,p+1):
        print(i,end="")
    print() 
    p=p+2