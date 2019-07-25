from itertools import permutations
puru=input()
queen=permutations(puru)
r=[]
for i in list(queen):
        s="".join(i)
        if s not in r:
             r.append(s)
for i in r:
      print(i)
