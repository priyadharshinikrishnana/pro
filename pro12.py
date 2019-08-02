name,nivi=map(int,input().split())
last=list(map(int,input().split()))
qwe=[]
for i in range(0,nivi):
     a,b=map(int,input().split())
     qwe.append([a,b])
for i in range(nivi):
     lower=qwe[i][0]
     upper=qwe[i][1]
     viji=sum(last[lower-1:upper])
     print(viji)
