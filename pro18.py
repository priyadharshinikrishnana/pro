priya,nivi=map(int,input().split())
log=[]
soo=0
for i in range(priya):
    sak.append(list(map(int,input().split())))   
for i in range(priya):
    for j in range(nivi-1):
        for k in range(j+1,nivi+1):
            if log[i][j:k]==[1]*len(log[i][j:k]):
                 if all(log[p+i][j:k]==[1]*len(log[p+i][j:k]) for p in range(len(log[i][j:k])-1)):
                     if len(log[i][j:k])>tel:
                        soo=len(log[i][j:k])
if len(log)==1 and len(log[0])==1 and log[0][0]==1:
    print(1)
for i in range(soo):
    print(*[1]*soo)
