n=int(input("enter the number"))
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end="")
    print()
    k=k+2