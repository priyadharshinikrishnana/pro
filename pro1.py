priya = int(input())
a=[]
for i in range(0,priya):
 zan=input()
 a.append(zan)
apple=[]
for i in zip(*a):
 if(i.count(i[0])==len(i)):
  apple.append(i[0])
 
 else:
  break
print(''.join(apple))
