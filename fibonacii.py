num = int(input("enter a num"))
s=0
x=0
y=1
print(x)
print(y)
for i in range(num):
    s=x+y
    print(s)
    x=y
    y=s
