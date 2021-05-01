num = int(input("enter a num"))
n=1
for row in range(1,num+1):
    for col in range(1,row+1):
        print(n,end="")
        n=n+1
    print()