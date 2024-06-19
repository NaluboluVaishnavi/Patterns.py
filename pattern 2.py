n = int(input())
for i in range(n,0,-1):
    a =[]
    for j in range(n,0,-1):
        a+=[j]*i
        print(*a,sep=" ",end=" ")
        print()