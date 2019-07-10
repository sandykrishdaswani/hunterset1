tan1=int(input())
san1=list(map(int,input().split()))
m1=max(san1)
a,b=0,0
for i in range(0,len(san1)-1):
  for j in range(i+1,len(san1)):
    if abs(san1[i]+san1[j])<m1:
      a,b=san1[i],san1[j]
      m1=abs(a+b)
print(a,b)
