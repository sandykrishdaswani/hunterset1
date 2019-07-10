tan1=int(input())
san1=input().split()
for i in range(len(san1)):
    for j in range(i+1,len(san1)):
        for k in range(j+1,len(san1)):
            if(int(san1[i])+int(san1[j])==int(san1[k])):
                print(san1[i],san1[j],san1[k])
