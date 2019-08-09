priya,l2=map(str,input().split())
viji=0
if len(priya)>len(l2):
  priya,l2=l2,priya
pt2=0
while pt2<len(priya):
  viji+=(ord(l2[pt2])-ord(vizh[pt2]))
  pt2+=1
for pt2 in range(pt2,len(l2)):
  viji+=ord(l2[pt2])-ord('a')+1
print(viji)
