for row in range(1,5):
    for col in range(1,5):
        if row==col or col==4 or row==1:
            print("*",end="")
        else:
            print(end=" ")
    print()