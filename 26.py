priya = int(input())
laa = list(map(int, input().split()))
maximum = 0
vvv = 0
any = laa[0]
for i in range(0,priya-1):
    if any < vvv[i+1]:
        vvv +=1
        any = vvv[i+1]
    else:
        if max(vvv[i+1:]) < any:
            any = laa[i+1]
print(vvv+1)
