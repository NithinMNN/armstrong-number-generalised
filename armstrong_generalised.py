import math as m
n=int(input("enter the no= "))
org=n
L=int(m.log10(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**(L+1))
    n=n//10
if org==sum:
    print(f"{org} is an Armstrong Number")
else:
    print(f"{org} is not an Armstrong Number")
