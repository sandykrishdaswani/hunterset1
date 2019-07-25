sandy,krish=map(int,input().split())
l=list(map(int,input().split()))
l.remove(krish)
rl=[]
for i in range(3):
    mi=abs(l[0]-krish)
    rr=l[0]
    for j in l:
        if abs(j-krish)<mi:
            rr=j
            mi=abs(j-krish)
    rl.append(rr)
    l.remove(rr)
for i in range(2):
    print(rl[i],end=" ")
print(rl[2]) 
