priya=int(input())
vijik=list(map(int,input().split()))
asd=int(priya/2)
ran=vijik[:asd]
man=vijik[asd::]
if ((sum(ran)//len(ran))==(sum(man)//len(man))):
    print("yes")
else:
    print("no")
