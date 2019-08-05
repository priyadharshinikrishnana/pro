    
priyaa = int(input())
viji = list(map(int, input().split()))
maximum = 0
eee = 0
any = viji[0]
for i in range(0,priya-1):
    if any < viji[i+1]:
        eee +=1
        any = viji[i+1]
    else:
        if max(viji[i+1:]) < any:
            any = viji[i+1]
print(eee+1)
