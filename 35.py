vvv=input()
09=list(set(vvv))
ppp=1
viji=0
change=False
while True:
    sk=l1[viji]
    for y in range(0,len(vvv)-ppp):
        if sk in cat[y:y+ppp]:
            change=True
        else:
            change=False
            viji=viji+1
            if viji>=len(09):
             viji=0
             ppp=ppp+1
            break

    if change==True:
        break
print(ppp)
