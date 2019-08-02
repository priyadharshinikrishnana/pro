priya,nivi=map(int,input().split())
moon=[]
soo=0
for i in range(priya):
    moon.append(list(map(int,input().split())))   
for i in range(priya):
    for j in range(nivi-1):
        for k in range(j+1,nivi+1):
            if moon[i][j:k]==[1]*len(moon[i][j:k]):
                 if all(moon[p+i][j:k]==[1]*len(moon[p+i][j:k]) for p in range(len(moon[i][j:k])-1)):
                     if len(moon[i][j:k])>tel:
                        soo=len(moon[i][j:k])
if len(moon)==1 and len(moon[0])==1 and moon[0][0]==1:
    print(1)
for i in range(soo):
    print(*[1]*soo)
