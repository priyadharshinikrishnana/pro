priya=input()
fish=0
for i in range(0,len(priya)-1):
  for j in range(i+1,len(priya)):
    if priya[i]<priya[j]:
      fish=1
      print(bhpriya[j:])
      break
  if fish==1:
    break
else:
  print(priya)
