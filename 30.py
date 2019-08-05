#vsb
hoo=(input())
rat=0
for i in range(0,len(hoo)):
    ppp=(hoo[:i]+hoo[i+1:])
    if(int(ppp) % 8==0):
       rat=1
        break
if(rat==1):
    print("yes")
else:
    print("no")
