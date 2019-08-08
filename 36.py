priya=input()
viji=list(map(int,input().split()))
kvp=0
for i in range(0,len(viji)-2):
    for j in range(i+1,len(viji)-1):
        for k in range(j+1,len(viji)):
            if viji[i]>viji[j] and viji[j]>viji[k]:
                kvp+=1
print(kvp)
