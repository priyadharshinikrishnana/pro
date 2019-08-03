viji=int(input())
priya=list(map(int,input().split()))[:viji]
m=sum(priya[0:viji:2])
son=sum(priya[1:viji:2])
if m>son:
  print(m)
else:
  print(son)
