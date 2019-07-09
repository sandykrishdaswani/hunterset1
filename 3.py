zx = int(input())
san = [x for x in input().split()]
san1 = []
for i in range(len(san)):
    if san[i] == str(i):
        san1.append(san[i])
    # print(i, san[i])

if len(san1) == 0:
    print('-1')
else:
    print(' '.join(sorted(san1)))
