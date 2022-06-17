n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,i+1):
        k=i*j
        print(k,end="")
    print()