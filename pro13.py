nn,mm=map(int,input().split())
chlm=[]
vinn=[]
priya=[int(m) for m in input().split() ]
for i in range(0,mm):
    a1,b1=map(int,input().split())
    for j in range(a1-1 ,b1):
        vinn.append(priya[j])
    mah=sorted(vinn)
    qwe.append(min(vinn))
    del vinn[:]
for z in range(0,len(qwe)):
    print(qwe[z])
