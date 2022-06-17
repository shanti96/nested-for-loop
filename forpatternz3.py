n=int(input("enter the number"))
p=n
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,p+1):
        print(j,end="")
    print()
    p=p-1