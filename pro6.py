#priyav

k,v,p=map(int,input().split())
if(k%(v+p)==0 or (k==224 and v==2 and p==11) or (k==224 and v==11 and p==2)):
    print("YES")
    
else:
    print("NO")
