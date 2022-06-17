n=int(input("enter the number"))
for i in range(0,n):
    for j in range(n,i,-1):
        print(j,end="")
    print()