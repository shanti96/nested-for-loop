n=input("enter the name")
i=len(n)
for p in range(1,i+1):
    for j in range(0,p):
        print(n[j],end="")
    print()