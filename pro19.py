asd=int(input())
priya=[]
uuu=[]
for i in range(asd):
    priya.append(list(map(int,input().split())))
for asd in priya:
    for num in asd:
        uuu.append(num)
uuu.sort()
for i in uuu:
    print(i,end=' ')
