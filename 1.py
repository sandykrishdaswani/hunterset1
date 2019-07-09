number=int(input())
l1=list(map(int,input().split()[:number]))
count=0
sk=[]
for i in range(0,number+1):
   if(l1.count(i)>1):
      sk.append(i)
if(len(sk)==0):
   print("unique")
kl=sorted(sk)
print(' '.join(map(str,kl)))
