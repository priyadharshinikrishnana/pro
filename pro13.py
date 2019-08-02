p,q=map(int,input().split())
ab=[]
stu=[]
viji=[int(n) for n in input().split() ]
for i in range(0,q):
    a1,b1=map(int,input().split())
    for j in range(a1-1 ,b1):
        stu.append(viji[j])
    pri=sorted(stu)
    ab.append(min(stu))
    del stu[:]
for z in range(0,len(ab)):
    print(ab[z])
