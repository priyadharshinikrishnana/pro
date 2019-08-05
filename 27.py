priya,aa=map(int,input().split())
vv=list(map(int,input().split()))
vpk=list(map(int,input().split()))
soan=[]
oin=0
for i in range(priya):
    o=vpk[i]/vv[i]
    soan.append(o)
while aa>=0 and len(soan)>0:
    mindex=soan.index(max(soan))
    if aa>=vv[mindex]:
        oin=oin+vpk[mindex]
        aa=aa-vv[mindex]
    vv.pop(mindex)
    vpk.pop(mindex)
    soan.pop(mindex)
print(oin)
