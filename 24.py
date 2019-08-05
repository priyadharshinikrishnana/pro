priya=int(input())
subha=2**priya
v=[]
for i in range(0,subha):
    p=bin(i)[2:].vfill(priya)
    if(len(p)<len(bin(2**priya-1)[2:])):
        v.append([p.count("1"),l])
    else:
        v.append([p.count("1"),l])
v.sort()
for i in range(len(v)):
    print(v[i][1])
