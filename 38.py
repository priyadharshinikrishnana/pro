vv,pp=map(int,input().split())
rrr = list(map(int,input().split()))
ii = 0
for i in range(0,len(rrr)):
    if (rrr[i]+pp)<=5:
        ii+=1
print(ii//3)
