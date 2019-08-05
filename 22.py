srt=int(input())
bjh=list(map(int,input().split()))[:srt]
zex=sum(bjh[0:srt:2])
yop=sum(bjh[1:srt:2])
if zex>yop:
  print(zex)
else:
  print(yop)
