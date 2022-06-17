n=int(input("enter the number"))
for i in range(n,0,-1):
    a=65
    for j in range(i,0,-1):
        print(chr(a),end="")
        a=a+1
    print()