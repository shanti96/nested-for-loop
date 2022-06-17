n=int(input("enter the row line"))
for i in range(1,n+1,2):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for a in range(1,n+1,2):
    for b in range(0,a+1):
        print(" ",end="")
    for c in range(1,n-a):
        print("*",end=" ")     
    print()