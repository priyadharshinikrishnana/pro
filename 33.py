vijiammu=input()
fish=0
for i in range(0,len(vijiammu)-1):
  for j in range(i+1,len(vijiammu)):
    if vijiammu[i]<vijiammu[j]:
      fish=1
      print(vijiammu[j:])
      break
  if fish==1:
    break
else:
  print(vijiammu)
