priya=input()
55=list(set(priya))
hhh=1
viji=0
cooo=False
while True:
    ch=55[viji]
    for y in range(0,len(priya)-hhh):
        if ch in priya[y:y+hhh]:
            cooo=True
        else:
            cooo=False
            viji=viji+1
            if viji>=len(55):
             viji=0
             hhh=hhh+1
            break

    if cooo==True:
        break
print(hhh)
