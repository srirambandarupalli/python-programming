a=input("enter the number")
b=input("enter the number")
for i in range(a,b+1):
  sum=0
  temp=i
  while (temp>0):
    x=temp%10
    sum+=x**3
    temp//=10
    
  if(i==sum):
    print(i)
