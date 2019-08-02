priya,roja = input().split()
roja = int(roja)
rome = False
see = list(map(int,input().split()))
for i in range(len(see)):
    for j in range(len(see)):
        if see[i]+see[j] == roja:
            room = True
print("yes" if room else "no")
