priya=int(input())
viji=2**priya
u=[]
for i in range(0,viji):
    l=bin(i)[2:].ufill(priya)
    if(len(l)<len(bin(2**priya-1)[2:])):
        u.append([l.count("1"),l])
    else:
        u.append([l.count("1"),l])
u.sort()
for i in range(len(u)):
    print(u[i][1])
