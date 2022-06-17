n=int(input("enter the number"))
p=1
for i in range(1,n):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,p+1):
        print("*",end="")
    print()
    p=p+2