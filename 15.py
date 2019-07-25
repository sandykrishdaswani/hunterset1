sandy=int(input())
l=list(map(int, input().split()))[:sandy]
mx=max(l)
funl=[]
for i in range(0,len(l)):
    new=l[i:]
    fix=max(new)
    if(l[i]==fix):
        funl.append(l[i])
print(*funl)
print(mx)
