vpo=(input())
nnn=0
for i in range(0,len(vpo)):
   fff=(vpo[:i]+vpo[i+1:])
    if(int(fff) % 8==0):
        nnn=1
        break
if(nnn==1):
    print("yes")
else:
    print("no")
