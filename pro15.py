priyak=input()
vijik=map(int,input().split())
user=[]
for i in vijik:
    coll=bin(i)
    user.append(coll)
fine=sorted(user)
fine.reverse()
for j in fine:
    print(int(j,2))
