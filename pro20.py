priya,viji=(map(int,input().split())
msd=list(map(int,input().split()))
msd.sort()
msd.reverse()
a=viji
poo=0
for i in msd:
    if(a>=i):
        sad=int(a/i)
        poo=poo+sad
        a=a-sad*i
    if a==0:
        break
if(a==0):
   print(poo)
else:
   print("it's not posiible to select coins in such a way that they sum upto",viji)
