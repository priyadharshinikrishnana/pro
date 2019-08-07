priya,viji = map(int,input().split())
subu=0
lala = []
for i in range(priya):
      lala.append(input())
for i in range(priya):
      for j in range(viji-1):
            if lala[i][j] != 'R' and lala[i][j+1] != 'R' :
                  subu+=3
            elif lala[i][j] != 'G' and lala[i][j+1] != 'G':
                  subu+=5
print(subu)
