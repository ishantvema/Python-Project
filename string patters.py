string = str(input("enter a string"))
leng=len(string)
for row in range(leng):
    for col in range(row+1):
        print(string[col],end="")
    print()