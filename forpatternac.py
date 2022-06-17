n=int(input("enter the number"))
k=65
for i in range(1,n):
    for j in range(1,i+1):
        print(chr(k),end="")
        k=k+1
    print()