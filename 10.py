tan1,san1=map(int,input().split())
s1=list(map(int,input().split()))
p1=list(map(int,input().split()))
if set(p1).issubset(set(s1)):
    print("YES")
else:
    print("NO")
