san,keer = map(int,input().split())
leny2 = list(map(int,input().split()))
leny3 = list(map(int,input().split()))
fk =1
for i in leny3:
    if i not in leny2:
        print('NO')
        f = 0
        break
if(fk):
    print('YES')
