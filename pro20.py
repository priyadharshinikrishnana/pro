priya,viji=map(int,input().split())
msd=list(map(int,input().split()))
asd.sort()
asd.reverse()
a=viji
ooo=0
for i in msd:
    if(a>=i):
        any=int(a/i)
        ooo=ooo+any
        a=a-any*i
    if a==0:
        break
if(a==0):
   print(ooo)
else:
   print("it's not posiible to select coins in such a way that they sum upto",viji)
