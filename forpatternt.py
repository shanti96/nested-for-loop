n=int(input("enter the number"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
        for p in range(0,1):
            print(" ",end="")
    print()