priya,l1=map(str,input().split())
viji=0
if len(priya)>len(l1):
  priya,l1=l1,priya
pt1=0
while pt1<len(priya):
  viji+=(ord(l1[pt1])-ord(vizh[pt1]))
  pt1+=1
for pt1 in range(pt1,len(l1)):
  viji+=ord(l1[pt1])-ord('a')+1
print(viji)
