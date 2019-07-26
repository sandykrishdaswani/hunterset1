xoo1,ball1=map(int,input().split())
l=[]
cs=0
ks=[]
for i in range(xoo1,ball1+1):
        l.append(bin(i)[2::])
for i in range(0,len(l)):
        ks.append(l[i].count("1"))
 
for i in range(0,len(ks)):
        if ks[i]!=1 and ks[i]!=2:
                for ps in range(2,ks[i]):
                        if ks[i]%ps==0:
                                break
                if ps==ks[i]-1:
                        cs=cs+1
        elif k[i]==2:
                cs=cs+1
print(cs)
