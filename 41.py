vv,pp=input().split()
vv=int(vv)
pp=int(pp)
priya=''
viji=2
if(vv+pp<=3):
    for i in range(0,vv+pp):
        if(i%2!=0):
            priya=priya+'0'
        else:
            priya=priya+'1'
else:    
    for i in range(0,vv+pp):
        if(i==viji):
            priya=priya+'0'
            if(viji==pp):
                viji=viji+2
            else:
                viji=viji+3
        else:
            priya=priya+'1'
x=len(priya)-1
if(int(priya[x])==0):
    print('-1') 
elif vv==1 and pp==2: 
     print("011")
else:
    print(priya)
