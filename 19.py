xam,toy=map(int,input().split())
l=[]
for i in range(xam):
    z=set(map(int,input().split()))
    l.append(z)
number=z.intersection(*l)
print(*number)
