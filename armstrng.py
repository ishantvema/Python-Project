num=int(input("enter a no "))
sum=0
rem=0
orig=num
u=str(num)
n=len(u)
print(n)
while num!=0:
    rem=num%10
    sum=sum+rem**n
    num=num//10

if orig==sum:
    print("num is armstrong",num)
else:
    print("not ",num)