ammu=int(input())
vpv=input().split()
vv=[]
for i in range(ammu):
    vijii=vpv[i]
    for j in range(i+1,ammu):
        if(int(vpv[i])<int(vpv[j]))and (int(vpv[j-1])<int(vpv[j])):
            vijii+=vpv[j]
        else:
            break
    vv.append(len(vijii))
print(max(vv))
