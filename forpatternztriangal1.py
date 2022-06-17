n=int(input("enter the number of row line"))
for i in range(1,n+1):
    for j in range(1,n*2):
        if i==n or j+i==n+1 or j-i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()            