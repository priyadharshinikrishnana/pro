subha,priya=map(int,input().split())
last=list(map(int,input().split()))
lin=[]
for i in range(0,priya):
     x,y=map(int,input().split())
     lin.append([x,y])
for i in range(priya):
     lower=lin[i][0]
     upper=lin[i][1]
     vijay=sum(last[lower-1:upper])
     print(vijay)
