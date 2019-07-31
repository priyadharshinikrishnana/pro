end=int(input())
bin=[int(i) for i in input().split()]
hen=0
for k in range(end):
   for j in range(k):
      if bin[j]<bin[k]:
         hen+=bin[j]
print(hen) 
