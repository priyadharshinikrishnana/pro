import math
priya,viji=map(int,input().split())
subha=[]
kvp=list(map(int,input().split()))
for i in range(0,viji):
    aaa,bbb=map(int,input().split())
    subha.append([aaa,bbb])
for i in subha:
    asd=i[0]-1
    lkj=i[1]-1
    print(math.gcd(kvp[asd],kvp[lkj]))
