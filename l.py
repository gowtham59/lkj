n1,q2=map(int,input().split())
b3=list(map(int,input().split()))
for x in range (q2):
    s4,t5=map(int,input().split())
    y=0
    for a in range(s4-1,t5):
        y=y^b3[a]
    print(y)
