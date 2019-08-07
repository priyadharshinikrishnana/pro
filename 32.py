pri,subha=map(int,input().split())
rice=[]
for i in range(0,pri):
    pp=[int(sv) for sv in input().split()]
    rice.append(sorted(pp))
for i in range(0,len(rice[0])):
  #print(rice[i])
  for j in range(0,len(rice)-1):
    if rice[j][i]>rice[j+1][i]:
      rice[j][i],rice[j+1][i]=rice[j+1][i],rice[j][i]
for i in rice:
  print(*i)
