for row in range(1,6):
    for col in range(1,6):
        if row==col or col==1 or row==5:
            print("*",end="")
        else:
            print(end=" ")
    print()