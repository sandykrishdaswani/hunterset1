zx = int(input())
san = [x for x in input().split()]
san1 = sorted(san, reverse=True)
print(''.join(san1))
