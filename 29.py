ooo=int(input())
a=0
yyy=0
vp=[]
while a<90 and a<ooo:
  p=0
  for j in str(ooo-a):
    p+=int(j)
  if p+(ooo-a)==ooo:
    yyy+=1
    vp.append(ooo-a)
  a+=1
print(yyy)
for a in vp:
  print(a)
