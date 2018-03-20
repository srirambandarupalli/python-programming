a=int(input("enter the number"))
temp=0
for i in range(2,a/2+1):
  if(a%i==0):
    temp=temp+1
if(temp<=0):
  print("prime number")
else:
  print("not a prime number")
