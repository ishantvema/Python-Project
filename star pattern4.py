for row in range(0,4):
    for col in range(0,7):
        if row==3 or row+col==3 or col-row==3:
            print("*",end="")
        else:
            print(end=" ")
    print()