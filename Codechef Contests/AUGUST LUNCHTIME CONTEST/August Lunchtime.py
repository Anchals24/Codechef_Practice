#Problem1 : Programming Languages

T = int(input())
for t in range(T):
    I = input()
    I = I.split()
    A , B , A1 , B1 , A2 , B2 = int(I[0]) , int(I[1]) , int(I[2]), int(I[3]), int(I[4]), int(I[5])
    if A == A1 and B == B1:
        print("1")
    elif A == B1 and B == A1:
        print("1")
    elif A == A2 and B == B2:
        print("2")
    elif A == B2 and B == A2:
        print("2")
    else:
        print("0")

#Problem2 : 
#Solution1 : TLE

T = int(input())
for t in range(T):
    N = int(input())
    add = 0
    maxi = 0
    for n in range(1 , N+1):
        add = add + n 
        if add % 2 == 0:
            if add > maxi:
                maxi = n 
    print(maxi)
    
#Solution2 : Optimized

T = int(input())
for t in range(T):
    N = int(input())
    summ = N*(N+1)//2
    if summ % 2 == 0:
        print(N)
    else:
        print(N-1)

