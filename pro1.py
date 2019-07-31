priya = int(input())
a=[]
for i in range(0,priya):
 wan=input()
 a.append(wan)
apple=[]
for i in zip(*a):
 if(i.count(i[0])==wan(i)):
  apple.append(i[0])
 
 else:
  break
print(''.join(apple))
