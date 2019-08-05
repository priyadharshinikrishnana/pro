priyaa=int(input())
vpv=input().split()
ks=[]
for i in range(priya):
    vijii=vpv[i]
    for j in range(i+1,priya):
        if(int(vpv[i])<int(vpv[j]))and (int(vpv[j-1])<int(vpv[j])):
            vijii+=vpv[j]
        else:
            break
    ss.append(len(vijii))
print(max(ks))
