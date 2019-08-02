priya,sen = input().split()
nivi = int(nivi)
rome = False
see = list(map(int,input().split()))
for i in range(len(see)):
    for j in range(len(see)):
        if see[i]+see[j] == nivi:
            room = True
print("yes" if room else "no")
