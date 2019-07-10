san1  =input()
tan1 = list(map(int,input().split()))
for i in range(len(tan1)):
    if (i%2 == 0 and tan1[i]%2 !=0) or (i%2!= 0 and tan1[i]%2 == 0):
        print(tan1[i],end = " ")
