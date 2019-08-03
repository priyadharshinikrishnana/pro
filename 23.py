priya=int(input())
vijii=2**priya
a=[]
for i in range(0,vijii):
    u=bin(i)[2:].afill(priya)
    if(len(u)<len(bin(2**priya-1)[2:])):
        a.append([u.count("1"),u])
    else:
        a.append([u.count("1"),u])
a.sort()
for i in range(len(a)):
    print(a[i][1])
