sandy=input()
keer=[int(k) for k in input().split()]
for i in keer:
    if(keer.count(i)==1):
        print(i)
