priya=int(input())
ngoo=list(map(int,input().split()))
ngoo.sort()
seen=0
sooo=0
for i in range(len(ngoo)):
    if ngoo[i]>=seen:
        sooo=sooo+1
    seen=seen+ngoo[i]
print(sooo)
