vijii=int(input())
babyy=list(map(int,input().split()))
dds=[1]*vijii
for i in range(vijii):
    if i==0:
        if babyy[i]>babyy[i+1]:
            dds[i]=dds[i]+dds[i+1]
    elif i>0:
        if babyy[i]>babyy[i-1]:
            dds[i]=dds[i]+dds[i-1]
print(sum(dds))
