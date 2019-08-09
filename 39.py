priyaa,l1=map(str,input().split())
vijii=0
if len(priyaa)>len(l1):
  priyaa,l1=l1,priyaa
vp1=0
while vp1<len(priyaa):
  vijii+=(ord(l1vp1])-ord(priyaa[vp1]))
  vp1+=1
for vp1 in range(vp1,len(l1)):
  vijii+=ord(l1[vp1])-ord('a')+1
print(vijii)
