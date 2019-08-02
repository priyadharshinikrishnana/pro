priya=int(input())
mom=list(map(int,input().split()))
asd=int(priya/2)
ooo=mom[:asd]
vvv=mom[asd::]
if ((sum(ooo)//len(ooo)==(sum(vvv)//len(vvv)):
    print("yes")
else:
    print("no")
