priyaa,viji=map(int,input().split())
list1=list(map(int,input().split()))
priyaa=[]
list1.insert(0,0)
for y in range(viji):
     see=[]
     g=0
     r,y=map(int,input().split())
     for i in range(r,y+1):         
         g^=list1[i]     
     priyaa.append(g)
for y in priyaa:
     print(y)
