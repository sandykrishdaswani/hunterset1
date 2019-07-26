sandy=int(input())
lu1=list(map(int,input().split()))
ress=1
l=[]
for i in lu1:
  ress=ress*i
for i in lu1:
  l.append(ress//i)
print(*l)
