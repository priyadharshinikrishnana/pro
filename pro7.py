priya1=int(input())
priya2=list(map(int,input().split()))
viji=0
for x in range(len(priya2)-2):
    for y in range(x+1,len(priya2)-1):
        for z in range(y+1,len(priya2)):
            if priya2[x]<priya2[y]<priya2[z] and x<y<z:
                viji=viji+1
print(viji)
