nfg = int(input())
lak = list(map(int, input().split()))
maximum = 0
coc = 0
any = lak[0]
for i in range(0,nfg-1):
    if any < lak[i+1]:
        coc +=1
        any = lak[i+1]
    else:
        if max(lak[i+1:]) < any:
            any = lak[i+1]
print(coc+1)
