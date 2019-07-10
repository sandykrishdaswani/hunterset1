sandy=list(map(str,input()))
v=t=0
for i in range(0,len(sandy)-1):
  q1=sandy[i]
  if int(q1)!=0:
   for j in range(i+1,i+2):
    q1=q1+n[j]
    if int(q1)<27 and int(q1)>0: v=v+1
    elif int(q1)==0: v=v-1
    else: break
if v!=1: t=v%2
print(v+t+1)
